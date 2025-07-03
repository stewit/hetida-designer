from typing import Any

import pandas as pd


def load_csv(path: str, **kwargs: Any) -> pd.DataFrame:
    return pd.read_csv(path, dtype_backend="pyarrow", **kwargs)


def write_csv(df: pd.DataFrame, path: str, **kwargs: Any) -> None:
    df.to_csv(path, **kwargs)
