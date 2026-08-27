type FormContext = any;

type LookupConfig = {
  parentColumn: string;
  childColumn: string;
  childTable: string;
  relationColumn: string;
  activeColumn?: string;
};

export function registerDynamicLookupFilter(formContext: FormContext, config: LookupConfig): void {
  const parentAttribute = formContext.getAttribute(config.parentColumn);
  const childControl = formContext.getControl(config.childColumn);
  if (!parentAttribute || !childControl) return;

  const applyFilter = () => {
    const parent = parentAttribute.getValue()?.[0];
    if (!parent?.id) return;

    const id = normalizeGuid(parent.id);
    const activeCondition = config.activeColumn
      ? `<condition attribute='${config.activeColumn}' operator='eq' value='1' />`
      : "";

    const filter = `<filter type='and'>
      <condition attribute='${config.relationColumn}' operator='eq' value='${id}' />
      ${activeCondition}
    </filter>`;

    childControl.addCustomFilter(filter, config.childTable);
  };

  childControl.addPreSearch(applyFilter);
  parentAttribute.addOnChange(() => {
    formContext.getAttribute(config.childColumn)?.setValue(null);
  });
}

export function normalizeGuid(value: string): string {
  return value.replace(/[{}]/g, "");
}
