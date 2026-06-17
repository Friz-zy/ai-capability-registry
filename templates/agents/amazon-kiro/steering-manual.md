---
mode: manual
---

# Deployment Checklist

This steering file is activated manually with `#deployment-checklist`.

## Pre-deployment

1. Run full test suite
2. Check for security vulnerabilities
3. Verify environment variables are set
4. Confirm database migrations are ready

## Deployment

1. Build the project
2. Deploy to staging first
3. Run smoke tests on staging
4. Deploy to production