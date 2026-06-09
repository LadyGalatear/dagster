import dagster as dg

from assets.patient import asset as patient_asset, upstream_asset
from graphs.patient import F_IO_MANAGER_KEY, FIOManager

defs = dg.Definitions(
    assets=[upstream_asset, patient_asset],
    resources={F_IO_MANAGER_KEY: FIOManager(foo="bar")},
    
)