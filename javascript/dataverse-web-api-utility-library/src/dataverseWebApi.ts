export function normalizeGuid(value?: string | null): string | null {
  if (!value) return null;
  return value.replace(/[{}]/g, "").trim().toLowerCase();
}

export function escapeODataString(value: string): string {
  return value.replace(/'/g, "''");
}

export async function retrieveFirst<T>(
  table: string,
  query: string,
): Promise<T | null> {
  const result = await Xrm.WebApi.retrieveMultipleRecords(table, query);
  return result.entities.length > 0 ? (result.entities[0] as T) : null;
}

export async function retrieveAll<T>(
  table: string,
  query: string,
): Promise<T[]> {
  const records: T[] = [];
  let page = await Xrm.WebApi.retrieveMultipleRecords(table, query);
  records.push(...(page.entities as T[]));

  while (page.nextLink) {
    const nextQuery = page.nextLink.substring(page.nextLink.indexOf("?"));
    page = await Xrm.WebApi.retrieveMultipleRecords(table, nextQuery);
    records.push(...(page.entities as T[]));
  }

  return records;
}

export function lookupId(record: Record<string, unknown>, logicalName: string): string | null {
  const raw = record[`_${logicalName}_value`];
  return typeof raw === "string" ? normalizeGuid(raw) : null;
}
