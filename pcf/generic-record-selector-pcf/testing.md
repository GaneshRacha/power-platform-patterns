# Testing guide

Validate at minimum:

- new parent record before an ID exists
- existing parent with prior selections
- selecting and deselecting multiple values
- mutually exclusive/default values
- inactive reference values
- duplicate prevention
- network/API failure
- parent save and refresh
- control re-render without loss of selection state

A production implementation should also include unit tests around GUID normalization, selection diffing, and repository calls.
