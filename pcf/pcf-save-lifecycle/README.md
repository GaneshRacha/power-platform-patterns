# PCF Save Lifecycle & Dirty-State Handling

**Discipline:** PCF  
**Level:** Advanced  
**Technologies:** PCF, TypeScript, Dataverse Web API, Model-Driven Apps

## Summary

Pattern for coordinating PCF outputs, form dirty state, parent save timing, and Dataverse child-record persistence.

## Engineering challenge

A PCF can display changed state without the parent form recognizing that anything needs to be saved.

## Implementation approach

1. Use bound outputs for parent-visible state where appropriate.
2. Call notifyOutputChanged only when output state actually changes.
3. Distinguish new-record behavior from existing-record persistence.
4. Persist child data only when a stable parent identifier is available.

## Key considerations

- No dirty changes
- Create form
- Duplicate persistence
- Autosave
- Output loops

## Design decisions

- Parent and child persistence responsibilities are explicit rather than implicit.
- Output notifications are minimized to avoid render/save churn.
- New-record scenarios defer child persistence until a parent ID exists.

## Validation matrix

| Scenario | Expected behavior |
| --- | --- |
| Happy path | Intended record, configuration, or action is processed successfully. |
| Missing / null input | Pattern exits safely or returns a clear validation message. |
| Invalid configuration | Operation fails predictably without corrupting existing data. |
| Existing data | Previously saved values remain stable unless the rule explicitly requires an update. |
| Error / retry path | Failures are observable and do not silently create duplicate or inconsistent results. |

## Production-readiness lens

Before using this pattern in a production solution, validate maintainability, error handling, security, performance, test coverage, deployment behavior, and environment-specific configuration.

## Public portfolio boundary

This is a sanitized reusable engineering pattern. It intentionally excludes organization-specific schema names, URLs, records, credentials, solution exports, and proprietary business details.

## Portfolio

[View the interactive portfolio](https://power-platform-portfolio-olive.vercel.app/implementations/pcf-save-lifecycle/)

[← Back to PCF](../README.md)
