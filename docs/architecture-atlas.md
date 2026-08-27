# Power Platform Architecture Atlas

This page gives a visual map of the flagship engineering patterns in this repository. The diagrams are intentionally generic and use sanitized `demo_` concepts rather than organization-specific systems.

## 1. Reusable PCF selection architecture

```mermaid
flowchart LR
    A[Model-Driven App] --> B[Generic Record Selector PCF]
    B --> C[UI / React state]
    B --> D[Selection service]
    D --> E[(Dataverse source table)]
    D --> F[(demo_recordselection junction table)]
    F --> G[(Parent business record)]

    C -. notifyOutputChanged .-> B
    G -. existing selections .-> D
```

**Key idea:** keep rendering, Dataverse access, and persistence concerns separate. Persist multi-record selections explicitly when history, reporting, and relationship semantics matter.

[Open the Generic Record Selector PCF →](../pcf/generic-record-selector-pcf/)

---

## 2. Server-side consistency architecture

```mermaid
flowchart TD
    A[Dataverse Update] --> B{Plugin pipeline}
    B --> C[Filtering attributes / depth guard]
    C --> D[Business-key query]
    D --> E{Eligible related records?}
    E -- Yes --> F[Transactional updates]
    E -- No --> G[Exit without writes]
    F --> H[(Consistent Dataverse state)]
```

**Key idea:** business rules that must hold regardless of client belong on the server. The plugin limits reads/writes and prevents recursive synchronization.

[Open the Cross-Record Synchronization Plugin →](../plugins/cross-record-synchronization-plugin/)

---

## 3. Secure external service gateway

```mermaid
sequenceDiagram
    participant U as App / Flow
    participant A as Dataverse Custom API
    participant S as C# Service Layer
    participant T as OAuth Provider
    participant X as External REST API

    U->>A: Execute command
    A->>S: Validate request
    S->>T: Acquire access token
    T-->>S: Bearer token
    S->>S: Validate HTTPS + allowlisted host
    S->>X: Request + correlation ID
    X-->>S: External response
    S-->>A: Normalized result
    A-->>U: Structured response
```

**Key idea:** credentials and endpoint trust decisions remain server-side. Client applications receive a stable command contract rather than direct access to protected services.

[Open Secure Service Integration →](../custom-api/secure-service-integration/)

---

## 4. Effective-dated configuration and historical context

```mermaid
flowchart LR
    A[(Program / Type)] --> B[(Effective-Dated Configuration)]
    B --> C{Active at registration time?}
    C -- Yes --> D[(Transaction)]
    D -->|stores lookup| B
    B --> E[Later deactivated / replaced]
    D --> F[Historical reporting]
    F -->|still resolves original configuration| B
```

**Key idea:** a transaction keeps the configuration record that was valid when the transaction was created. Later configuration changes do not rewrite historical meaning.

[Open Effective-Dated Configuration →](../dataverse/effective-dated-configuration/)

---

## 5. Defensive Power Automate execution

```mermaid
flowchart TD
    A[Dataverse trigger] --> B{Record ID present?}
    B -- No --> Z[Controlled terminate / log]
    B -- Yes --> C[List rows with selective filter]
    C --> D{Rows found?}
    D -- No --> Z
    D -- Yes --> E[Resolve first row safely]
    E --> F[Idempotent record action]
    F --> G[Success / correlation logging]
    E -. exception .-> H[Catch scope]
    H --> I[Operational error record]
```

**Key idea:** never dereference `first()` or invoke a record action until the identifier/result has been validated.

[Open Defensive Dataverse Record ID Handling →](../power-automate/defensive-dataverse-recordid-flow/)

---

## 6. Team-based Dataverse security boundary

```mermaid
flowchart LR
    U1[Worker] --> R1[Least-privilege security role]
    U2[Supervisor] --> R2[Supervisor role]
    R1 --> T1[Owner Team A]
    R2 --> T1
    T1 --> A[(Team A records)]

    U3[Worker] --> R3[Least-privilege security role]
    R3 --> T2[Owner Team B]
    T2 --> B[(Team B records)]

    A -. not exposed by navigation alone .- B
```

**Key idea:** Model-Driven App navigation can improve UX, but the actual data boundary is Dataverse privileges, ownership, business units, teams, and sharing.

[Open Team-Based Data Security →](../security/team-based-data-security/)

---

## 7. Managed delivery and troubleshooting loop

```mermaid
flowchart LR
    A[Source-controlled solution] --> B[Build / unpack validation]
    B --> C[Managed package]
    C --> D[Target environment]
    D --> E{Import succeeds?}
    E -- Yes --> F[Smoke / regression validation]
    E -- No --> G[Classify failing component]
    G --> H[Compare source and target metadata]
    H --> I[Fix smallest root mismatch]
    I --> B
```

**Key idea:** solve the metadata mismatch at its source rather than layering workarounds on the target environment.

[Open Solution Import Troubleshooting →](../alm/solution-import-troubleshooting/)

---

## How the patterns fit together

```mermaid
flowchart TB
    UI[Power Apps / Power Pages] --> JS[JavaScript + PCF]
    JS --> DV[(Dataverse)]
    DV --> PL[Plugins + Custom APIs]
    DV --> PA[Power Automate]
    PL --> INT[Azure / External APIs]
    PA --> INT
    DV --> SEC[Teams + Security Roles]
    DV --> CFG[Configuration + Reference Data]
    UI --> CFG
    JS --> CFG
    PL --> CFG
    ALL[ALM / DevOps] --> UI
    ALL --> JS
    ALL --> PL
    ALL --> PA
    ALL --> CFG
```

The repository is organized around these boundaries so each pattern can be reviewed independently while still fitting into a larger enterprise solution architecture.
