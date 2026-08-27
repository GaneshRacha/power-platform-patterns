# Dataverse solution import troubleshooting playbook

## 1. Classify the failure

Start with the component type and exact error. Typical families include:

- missing/root component dependency
- attribute type mismatch
- primary-name mismatch
- duplicate relationship
- invalid Form XML / custom control metadata
- invalid FetchXML or missing primary key
- ownership mismatch
- PCF manifest/version contract mismatch
- app module / sitemap dependency

## 2. Compare source and target metadata

Do not repeatedly re-import the same ZIP. Determine whether the target already contains a conflicting definition or a dependency is absent.

## 3. Fix the smallest root mismatch

Prefer correcting component metadata or dependency sequencing over deleting unrelated target components.

## 4. Repackage and validate

Confirm solution dependencies, managed/unmanaged layers, component versions, and target environment configuration.

## 5. Smoke test after import

Validate forms, views, PCFs, plugins, flows, security, and navigation—not just the import result.

## Example diagnosis table

| Symptom | First checks |
| --- | --- |
| `String` vs `Lookup` | Existing target attribute type and source schema |
| Primary name conflict | Primary-name logical/schema name in both environments |
| Not a root component | Missing base entity/component dependency |
| Invalid custom control XML | PCF manifest version vs form metadata |
| Missing column in FetchXML | View references and target table metadata |
