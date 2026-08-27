# Power Platform Engineering Patterns

A public-safe library of **136 reusable engineering patterns** across Microsoft Power Platform, Dataverse, PCF, C# plugins, Custom APIs, Power Automate, Azure integration, analytics, ALM, security, and production engineering.

Live portfolio: https://power-platform-portfolio-olive.vercel.app/

## Flagship source implementations

These patterns include meaningful sanitized source/configuration in addition to documentation.

### Component & client engineering

- [Generic Record Selector PCF](pcf/generic-record-selector-pcf/) — TypeScript models, Dataverse repository layer, architecture, and testing guidance
- [Dynamic Dataverse Lookup Filtering](javascript/dynamic-lookup-filtering/) — reusable Model-Driven App lookup filtering source
- [Status-Based Field Locking](javascript/status-based-field-locking/) — configurable lifecycle-driven UI locking helper
- [Dataverse Web API Utility Library](javascript/dataverse-web-api-utility-library/) — GUID, lookup, OData, paging, and retrieval helpers

### Server-side & integration engineering

- [Cross-Record Synchronization Plugin](plugins/cross-record-synchronization-plugin/) — C# synchronization logic, eligibility rules, query minimization, and registration guidance
- [Parent/Child Calculation Plugin](plugins/parent-child-calculation-plugin/) — PreOperation calculation from structured child input
- [Secure Service Integration](custom-api/secure-service-integration/) — C# HTTPS/allowlist service gateway and Custom API contract
- [External REST API Integration](integration/external-rest-api-integration/) — reusable HTTP client with correlation IDs and controlled integration errors

### Dataverse, process & automation architecture

- [Effective-Dated Configuration](dataverse/effective-dated-configuration/) — sample schema, overlap/single-active rules, and historical lookup preservation
- [Configuration-Driven Status & BPF](architecture/configuration-driven-status-bpf/) — portable process/stage configuration example
- [Dataverse Business Calendar Engine](power-automate/business-calendar-engine/) — persisted calendar contract and ingestion/consumer design
- [Defensive Dataverse Record ID Handling](power-automate/defensive-dataverse-recordid-flow/) — guarded `List rows`, safe `first()`, error scopes, and idempotency guidance

### Security & ALM

- [Team-Based Data Security](security/team-based-data-security/) — owner-team architecture, role scope matrix, and role-combination guidance
- [Dataverse Solution Import Troubleshooting](alm/solution-import-troubleshooting/) — structured ALM diagnosis and recovery playbook
- [PCF Deployment & Version Management](alm/pcf-version-management/) — manifest/release version verification script and contract guidance

## Why this repository exists

The portfolio website explains the work visually. This repository provides the technical evidence behind it: source examples, configuration patterns, architecture decisions, validation scenarios, and production considerations.

The patterns are intentionally generic. Organization-specific schema names, tenant URLs, credentials, client data, proprietary solution exports, and internal source code are excluded.

## Library

- [ALM](alm/)
- [Architecture](architecture/)
- [Canvas Apps](canvas-apps/)
- [Custom API](custom-api/)
- [Data Engineering](data-engineering/)
- [Dataverse](dataverse/)
- [DevOps](devops/)
- [Integration](integration/)
- [JavaScript](javascript/)
- [Model-Driven Apps](model-driven-apps/)
- [PCF](pcf/)
- [Plugins](plugins/)
- [Power Automate](power-automate/)
- [Power BI](power-bi/)
- [Power Pages](power-pages/)
- [Production Engineering](production-engineering/)
- [Security](security/)

## Repository approach

Not every one of the 136 patterns needs a fake standalone app. Each implementation is documented, and the highest-value patterns are progressively upgraded with meaningful sanitized source files, configuration, architecture, and tests.

## Public-safety boundary

See [SANITIZATION.md](SANITIZATION.md). Public examples use generic aliases and omit credentials, tenant URLs, production identifiers, proprietary solution exports, internal documentation, and organization-specific business terminology.

## Related repository

Website source: https://github.com/GaneshRacha/power-platform-portfolio
