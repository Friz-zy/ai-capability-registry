"""Focused regression coverage for generated MCP security metadata."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from registry_lib import load_all


def load_generator_module():
    """Load the standalone MCP generator for direct rendering tests.

    Returns:
        The loaded generator module.
    """
    specification = importlib.util.spec_from_file_location(
        "generate_mcp", ROOT / "scripts" / "generate-mcp.py"
    )
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


class GenerateMcpTests(unittest.TestCase):
    """Verify MCP output preserves source metadata and safe web guidance."""

    @classmethod
    def setUpClass(cls):
        """Load the generator once for the focused suite."""
        cls.generator = load_generator_module()

    def hosted_server(self, **overrides):
        """Return a minimal hosted MCP record with explicit source metadata.

        Args:
            **overrides: Source fields to replace in the baseline record.

        Returns:
            A complete server record accepted by the MCP skill renderer.
        """
        server = {
            "id": "example-security-server",
            "name": "Example Security Server",
            "description": "Test server.",
            "source": {
                "type": "hosted_https",
                "hosted_url": "https://mcp.example.invalid/mcp",
                "authentication": "Reviewed custom header",
            },
            "security": {"permission_default": "manual_review"},
            "transport": {"type": "streamable_http"},
            "trust": "candidate",
            "runtime": "hosted_https",
            "default_mode": "manual_review",
            "keywords": ["security"],
            "skill": {},
        }
        server.update(overrides)
        return server

    def test_skill_renders_exact_security_metadata_and_candidate_warning(self):
        """Candidate server records retain metadata and require manual review."""
        content = self.generator.skill_content(self.hosted_server())

        self.assertIn("- Trust: `candidate`", content)
        self.assertIn("- Default mode: `manual_review`", content)
        self.assertIn("- Permission default: `manual_review`", content)
        self.assertIn("- Authentication: `Reviewed custom header`", content)
        self.assertIn("Trust is `candidate`; this server is not approved for automatic use.", content)
        self.assertIn("Complete manual review before connecting or invoking tools", content)

    def test_all_enabled_server_skills_render_declared_security_metadata(self):
        """Every enabled catalog record renders its complete per-server metadata."""
        servers = self.generator.enabled_servers(load_all()["mcp_servers"])

        self.assertTrue(servers)
        for server in servers:
            with self.subTest(server_id=server["id"]):
                security = server["security"]
                content = self.generator.skill_content(server)
                self.assertIn(f"- Trust: `{server['trust']}`", content)
                self.assertIn(f"- Default mode: `{server['default_mode']}`", content)
                self.assertIn(f"- Permission default: `{security['permission_default']}`", content)
                authentication = server["source"].get(
                    "authentication", "Unspecified in source metadata"
                )
                self.assertIn(f"- Authentication: `{authentication}`", content)

    def test_skill_warns_for_unknown_trust_and_unspecified_authentication(self):
        """Unknown source metadata cannot be rendered as an approved configuration."""
        server = self.hosted_server(
            source={"type": "hosted_https", "hosted_url": "https://mcp.example.invalid/mcp"},
            security={"permission_default": "ask_before_write"},
            trust="unknown",
            default_mode="ask_before_write",
        )
        content = self.generator.skill_content(server)

        self.assertIn("- Trust: `unknown`", content)
        self.assertIn("- Authentication: `Unspecified in source metadata`", content)
        self.assertIn("Trust is `unknown`; source metadata does not establish approval.", content)
        self.assertIn("Complete manual review before connecting or invoking tools", content)

    def test_skill_warns_for_manual_review_defaults(self):
        """Manual-review mode or permission metadata is visible and actionable."""
        server = self.hosted_server(
            security={"permission_default": "manual_review"},
            trust="trusted",
            default_mode="manual_review",
        )
        content = self.generator.skill_content(server)

        self.assertIn("Default mode is `manual_review`.", content)
        self.assertIn("Permission default is `manual_review`.", content)
        self.assertIn("Complete manual review before connecting or invoking tools", content)

    def test_connection_configuration_preserves_hosted_server_identity(self):
        """Security metadata rendering does not alter the established connection output."""
        configuration = self.generator.connection_config(self.hosted_server())

        self.assertEqual(
            {
                "mcpServers": {
                    "example-security-server": {
                        "type": "streamable_http",
                        "url": "https://mcp.example.invalid/mcp",
                    }
                }
            },
            configuration,
        )

    def test_web_guidance_uses_only_redacted_reviewed_authentication(self):
        """Web guidance excludes credential examples, URL keys, and scheme guessing."""
        content = (ROOT / "templates" / "mcp" / "web.md").read_text(encoding="utf-8")

        self.assertIn("<DOCUMENTED_HEADER_NAME>", content)
        self.assertIn("<REDACTED_SECRET_REFERENCE>", content)
        self.assertIn("Never place credentials in URL query strings.", content)
        self.assertIn("Do not log credential values", content)
        for forbidden_example in ("Bearer", "Basic", "?api_key=", "eyJ", "user:password"):
            self.assertNotIn(forbidden_example, content)


if __name__ == "__main__":
    unittest.main()
