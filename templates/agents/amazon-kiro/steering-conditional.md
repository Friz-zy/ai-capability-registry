---
condition: "*.ts"
---

# TypeScript Style Guide

Always use TypeScript strict mode. Prefer interfaces over type aliases for object shapes. Use `unknown` instead of `any`.

- Use explicit return types on exported functions
- Avoid non-null assertions; use proper type narrowing
- Use `enum` only for string enums