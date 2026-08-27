import type { SelectorConfig } from "../models/RecordOption";

export interface WebApiLike {
  retrieveMultipleRecords(entityLogicalName: string, query?: string): Promise<{ entities: Record<string, unknown>[] }>;
  createRecord(entityLogicalName: string, data: Record<string, unknown>): Promise<{ id: string }>;
  deleteRecord(entityLogicalName: string, id: string): Promise<unknown>;
}

export class SelectionRepository {
  constructor(private readonly api: WebApiLike, private readonly config: SelectorConfig) {}

  async getSelectedIds(parentId: string): Promise<Set<string>> {
    const normalizedParentId = normalizeGuid(parentId);
    const query = `?$select=_${this.config.selectedLookupColumn}_value&$filter=_${this.config.parentLookupColumn}_value eq ${normalizedParentId}`;
    const result = await this.api.retrieveMultipleRecords(this.config.selectionTable, query);
    return new Set(
      result.entities
        .map((row) => row[`_${this.config.selectedLookupColumn}_value`])
        .filter((value): value is string => typeof value === "string")
        .map(normalizeGuid)
    );
  }

  async add(parentId: string, selectedId: string): Promise<void> {
    const payload: Record<string, unknown> = {
      [`${this.config.parentLookupColumn}@odata.bind`]: `/${this.config.sourceTable}s(${normalizeGuid(parentId)})`,
      [`${this.config.selectedLookupColumn}@odata.bind`]: `/${this.config.sourceTable}s(${normalizeGuid(selectedId)})`,
    };
    await this.api.createRecord(this.config.selectionTable, payload);
  }
}

export function normalizeGuid(value: string): string {
  return value.replace(/[{}]/g, "").toLowerCase();
}
