# Architecture

```text
Model-driven form
   ↓
Generic Record Selector PCF
   ├─ UI state / selected IDs
   ├─ Dataverse Web API repository
   ↓
Explicit selection junction table
   ├─ Parent lookup
   └─ Selected record lookup
```

The control keeps rendering concerns separate from Dataverse persistence. An explicit junction table provides traceability, filtering, reporting, and future metadata on a selection relationship.

## Public schema aliases

Examples intentionally use generic names such as `demo_request`, `demo_recordselection`, and `demo_referencevalue` rather than organization-specific schema names.
