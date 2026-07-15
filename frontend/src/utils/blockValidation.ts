import type { BlockInfo, FieldSchema, PipelineBlock } from "../types";

function isFieldFilled(schema: FieldSchema, value: unknown): boolean {
  if (!schema.required) return true;
  if (schema.type === "array" && schema.items?.enum) {
    return Array.isArray(value) && value.length === schema.items.enum.length;
  }
  if (schema.type === "sub_block") {
    return (
      value !== null &&
      value !== undefined &&
      typeof value === "object" &&
      typeof (value as Record<string, unknown>).type === "string"
    );
  }
  if (value === undefined || value === null || value === "") return false;
  if (schema.type === "nested_model" && schema.properties) {
    return Object.entries(schema.properties).every(([sub, subSchema]) =>
      isFieldFilled(subSchema, (value as Record<string, unknown>)[sub]),
    );
  }
  return true;
}

export function blockHasUnfilledRequired(
  block: PipelineBlock,
  info: BlockInfo,
): boolean {
  return Object.entries(info.fields).some(
    ([name, schema]) => !isFieldFilled(schema, block.config[name]),
  );
}
