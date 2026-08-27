#!/usr/bin/env python3
from pathlib import Path
import re

CATEGORY_DIRS = [
    "alm", "architecture", "canvas-apps", "custom-api", "data-engineering",
    "dataverse", "devops", "integration", "javascript", "model-driven-apps",
    "pcf", "plugins", "power-automate", "power-bi", "power-pages",
    "production-engineering", "security",
]

pattern = re.compile(r"^- \[(.+?)\]\(([^/]+)/\) — (.+)$")
created = 0

for category in CATEGORY_DIRS:
    index_path = Path(category) / "README.md"
    if not index_path.exists():
        continue

    discipline = category.replace("-", " ").title()
    for line in index_path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line.strip())
        if not match:
            continue

        title, slug, level = match.groups()
        target = Path(category) / slug / "README.md"
        if target.exists():
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        content = f"""# {title}

**Discipline:** {discipline}  
**Level:** {level}

## Overview

This folder documents the reusable, public-safe engineering pattern represented in the portfolio implementation library.

## Engineering focus

- Clear client/server or platform responsibility boundaries
- Maintainable configuration and reusable design
- Defensive validation and error handling
- Security, ALM, testing, and production-readiness considerations

## Public portfolio boundary

Organization-specific schema names, tenant URLs, credentials, client data, proprietary solution exports, and confidential source code are intentionally excluded. Standalone sanitized code/configuration samples can be added here as they are prepared for public release.

## Portfolio

[View the interactive implementation](https://power-platform-portfolio-olive.vercel.app/implementations/{slug}/)

[← Back to {discipline}](../README.md)
"""
        target.write_text(content, encoding="utf-8")
        created += 1

print(f"Created {created} implementation documentation files")
