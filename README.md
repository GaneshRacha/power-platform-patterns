# Power Platform Engineering Patterns

A public-safe library of **136 reusable engineering patterns** across Microsoft Power Platform, Dataverse, PCF, C# plugins, Custom APIs, Power Automate, Azure integration, analytics, ALM, security, and production engineering.

Live portfolio: https://power-platform-portfolio-olive.vercel.app/

## Repository depth

The library has two deliberate levels of technical evidence:

- **136 documented patterns** — each pattern has a dedicated folder with implementation guidance and a discipline-appropriate technical example such as TypeScript, C#, Power Fx, JSON configuration, SQL, DAX, PowerShell, YAML, KQL, or flow design material.
- **15 flagship implementations** — deeper examples with stronger project structure, architecture/testing notes, reusable source, configuration contracts, and production-readiness guidance.

These are sanitized engineering examples, not copied customer solution exports. Schema aliases use `demo_` names and environment-specific identifiers, credentials, tenant URLs, and proprietary business details are intentionally excluded.

## Flagship source implementations

### Component & client engineering

- [Generic Record Selector PCF](pcf/generic-record-selector-pcf/) — PCF manifest, TypeScript control skeleton, models, Dataverse repository layer, package metadata, architecture, and testing guidance
- [Dynamic Dataverse Lookup Filtering](javascript/dynamic-lookup-filtering/) — reusable Model-Driven App lookup filtering source
- [Status-Based Field Locking](javascript/status-based-field-locking/) — configurable lifecycle-driven UI locking helper
- [Dataverse Web API Utility Library](javascript/dataverse-web-api-utility-library/) — GUID, lookup, OData, paging, retrieval helpers, TypeScript project metadata

### Server-side & integration engineering

- [Cross-Record Synchronization Plugin](plugins/cross-record-synchronization-plugin/) — C# synchronization logic, Dataverse project file, eligibility rules, query minimization, registration guidance, and behavior tests
- [Parent/Child Calculation Plugin](plugins/parent-child-calculation-plugin/) — PreOperation calculation from structured child input with plugin project metadata
- [Secure Service Integration](custom-api/secure-service-integration/) — C# HTTPS/allowlist service gateway and Custom API contract
- [External REST API Integration](integration/external-rest-api-integration/) — reusable HTTP client with correlation IDs and controlled integration errors

### Dataverse, process & automation architecture

- [Effective-Dated Configuration](dataverse/effective-dated-configuration/) — sample schema, overlap/single-active rules, and historical lookup preservation
- [Configuration-Driven Status & BPF](architecture/configuration-driven-status-bpf/) — portable process/stage configuration example
- [Dataverse Business Calendar Engine](power-automate/business-calendar-engine/) — persisted calendar contract and ingestion/consumer design
- [Defensive Dataverse Record ID Handling](power-automate/defensive-dataverse-recordid-flow/) — guarded `List rows`, safe `first()`, error scopes, idempotency guidance, and validation matrix

### Security & ALM

- [Team-Based Data Security](security/team-based-data-security/) — owner-team architecture, role scope matrix, implementation checklist, and role-combination guidance
- [Dataverse Solution Import Troubleshooting](alm/solution-import-troubleshooting/) — structured ALM diagnosis and recovery playbook
- [PCF Deployment & Version Management](alm/pcf-version-management/) — manifest/release version verification script and contract guidance

## Why this repository exists

The portfolio website explains the work visually. This repository provides the technical evidence behind it: source examples, configuration patterns, architecture decisions, validation scenarios, and production considerations.

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

## Engineering standards used in the examples

- Minimal Dataverse column selection and guarded lookup/GUID handling
- Clear client/server responsibility boundaries
- Idempotent automation where retries are possible
- Plugin depth/filtering/image guidance and thin plugin entry points
- Environment-specific configuration kept out of source code
- Explicit error paths, correlation values, and production observability
- Historical configuration/reference preservation where point-in-time reporting matters
- UI visibility treated as UX, never as a replacement for Dataverse security

## Public-safety boundary

See [SANITIZATION.md](SANITIZATION.md). Public examples omit credentials, tenant URLs, production identifiers, proprietary solution exports, internal documentation, and organization-specific business terminology.

## Related repository

Website source: https://github.com/GaneshRacha/power-platform-portfolio
