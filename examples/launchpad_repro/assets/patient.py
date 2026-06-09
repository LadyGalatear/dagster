import dagster as dg

from graphs import patient
upstream_asset = dg.SourceAsset(
    dg.AssetKey(["private_gold", "dbt_table_input"])
)

MY_PREFIX = ["my_prefix"]
PRIVATE_GOLD_PREFIX = ["private_gold"]



asset = dg.AssetsDefinition.from_graph(
    patient.patient_graph,
    key_prefix=MY_PREFIX,
    owners_by_output_name={"patient": ["me@example.com"]},
    keys_by_input_name={
        "dbt_table_input": dg.AssetKey(
            PRIVATE_GOLD_PREFIX + ["dbt_table_input"]
        )
    },
    tags_by_output_name={
        "patient": {
            "foo": "bar",
        }
    },
    automation_conditions_by_output_name={
        "patient": dg.AutomationCondition.eager(),
    },
)