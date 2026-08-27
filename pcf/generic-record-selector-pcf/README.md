# Generic Record Selector PCF

**Discipline:** PCF  
**Level:** Advanced  
**Technologies:** PCF, TypeScript, Dataverse Web API, React

## Summary

Reusable PCF pattern for selecting multiple records and persisting selections through an explicit Dataverse child/junction table.

## Engineering challenge

Build one reusable selector instead of creating a separate custom control for every multi-record business scenario.

## Implementation approach

1. Parameterize the data source and parent record context.
2. Load existing selections during control initialization.
3. Persist selections using an explicit Dataverse record-selection entity.
4. Support default and mutually exclusive options without overwriting existing data.

## Key considerations

- New vs. existing records
- Parent save lifecycle
- Form dirty state
- Duplicate prevention
- Inactive source values

## Design decisions

- Why an explicit junction table was preferable to a multi-select Choice.
- How PCF lifecycle events affect parent/child persistence.
- How the design was made reusable across scenarios.

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

[View the interactive portfolio](https://power-platform-portfolio-olive.vercel.app/implementations/generic-record-selector-pcf/)

[← Back to PCF](../README.md)
