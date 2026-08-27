# Custom API contract

Example command: `demo_InvokeExternalService`

Inputs:

- `RequestJson` — sanitized JSON request payload
- `Operation` — controlled operation name, not an arbitrary URL

Outputs:

- `Success` — boolean
- `ResponseJson` — normalized JSON response
- `CorrelationId` — identifier for support/tracing

The Custom API should resolve endpoints and secrets from server-side configuration. Client code must never supply client secrets or unrestricted URLs.
