export interface RecordOption {
  id: string;
  label: string;
  selected: boolean;
  disabled?: boolean;
}

export interface SelectorConfig {
  sourceTable: string;
  sourceIdColumn: string;
  sourceLabelColumn: string;
  selectionTable: string;
  parentLookupColumn: string;
  selectedLookupColumn: string;
}
