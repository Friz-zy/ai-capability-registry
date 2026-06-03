# Mobile App Workflow

Use this workflow when the user wants to build an iOS, Android, Flutter, React Native, native, cross-platform, or mobile-first app.

## Files

- Manifest: `workflows/product-delivery/mobile-app/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow adds platform decisions, offline behavior, push notifications, app permissions, store review, signing, and limited rollback constraints. Do not treat mobile releases like web releases.

Use staged parallel delegation inside each stage, then validate outputs against the manifest acceptance criteria before continuing.
