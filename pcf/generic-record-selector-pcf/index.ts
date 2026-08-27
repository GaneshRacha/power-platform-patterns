import { SelectorConfig, RecordOption } from "./src/models/RecordOption";
import { DataverseSelectionRepository } from "./src/services/DataverseSelectionRepository";

export class GenericRecordSelector implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private notifyOutputChanged!: () => void;
  private value = "";
  private options: RecordOption[] = [];

  public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void): void {
    this.notifyOutputChanged = notifyOutputChanged;
    this.value = context.parameters.value.raw ?? "";
  }

  public async updateView(context: ComponentFramework.Context<IInputs>): Promise<void> {
    const config: SelectorConfig = {
      sourceTable: context.parameters.sourceTable.raw ?? "demo_reference",
      sourceIdColumn: context.parameters.sourceIdColumn.raw ?? "demo_referenceid",
      sourceLabelColumn: context.parameters.sourceLabelColumn.raw ?? "demo_name",
      selectionTable: "demo_recordselection",
      parentLookupColumn: "demo_parentid",
      selectedLookupColumn: "demo_selectedrecordid",
    };

    const repository = new DataverseSelectionRepository(context.webAPI, config);
    this.options = await repository.loadOptions();
  }

  public setSelectedIds(ids: string[]): void {
    this.value = JSON.stringify([...new Set(ids)]);
    this.notifyOutputChanged();
  }

  public getOutputs(): IOutputs {
    return { value: this.value };
  }

  public destroy(): void {}
}

interface IInputs {
  value: ComponentFramework.PropertyTypes.StringProperty;
  sourceTable: ComponentFramework.PropertyTypes.StringProperty;
  sourceIdColumn: ComponentFramework.PropertyTypes.StringProperty;
  sourceLabelColumn: ComponentFramework.PropertyTypes.StringProperty;
}

interface IOutputs { value?: string; }
