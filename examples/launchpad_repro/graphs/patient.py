import dagster as dg
import pandas as pd
from enum import Enum


F_IO_MANAGER_KEY = "f_io_manager"
F_ENDPOINT_KEY = "endpoint"
F_METHOD_KEY = "method"

class FRequestMethod(Enum):
    PUT = "PUT"


class Patient:
    pass


class FIOManager(dg.IOManager):
    def __init__(self, foo: str):
        self.foo = foo

    def handle_output(self, context, obj):
        pass

    def load_input(self, context):
        return pd.DataFrame()

@dg.op(
    out=dg.Out(
        io_manager_key=F_IO_MANAGER_KEY,
        metadata={
            F_ENDPOINT_KEY: "patients",
            F_METHOD_KEY: FRequestMethod.PUT.value,
        },
    ),
)
def get_patients(dbt_table_input: pd.DataFrame) -> list[Patient]:
    """some logic"""

    return [Patient()]


@dg.graph(
    name="patient",
    ins={"dbt_table_input": dg.GraphIn()},
    out={"patient": dg.GraphOut()},
)
def patient_graph(dbt_table_input):  
    return get_patients(dbt_table_input)