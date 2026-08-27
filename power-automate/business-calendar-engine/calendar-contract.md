# Dataverse Business Calendar Contract

## Table

`demo_businesscalendar`

| Column | Type | Example |
| --- | --- | --- |
| `demo_date` | Date Only | `2026-11-26` |
| `demo_dayofweek` | Text | `Thursday` |
| `demo_holidayname` | Text | `Example Holiday` |
| `demo_observedyear` | Whole Number | `2026` |
| `demo_isworkingday` | Yes/No | `false` |

## Ingestion flow

1. Scheduled or manually triggered refresh.
2. Retrieve holiday/reference feed.
3. Parse and normalize dates.
4. Upsert by date/year business key.
5. Mark weekends and holidays as non-working days.
6. Record refresh timestamp and failures.

## Consumer query

A validation rule queries the exact date and reads `demo_isworkingday`; it does not hard-code holiday names in JavaScript or Power Fx.

## Why persist locally

Persisting calendar reference data makes validation deterministic, reportable, and resilient to temporary upstream API failures.
