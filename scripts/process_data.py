"""Download, clean, validate, and export the public Iris dataset."""

from pathlib import Path

import pandas as pd


DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "iris_clean.csv"
REQUIRED_COLUMNS = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species",
]
MEASUREMENT_COLUMNS = REQUIRED_COLUMNS[:-1]


def main() -> None:
    """Run the pipeline and print a concise quality summary."""
    df = pd.read_csv(DATA_URL)
    rows_downloaded = len(df)

    # Standardize column names and coerce measurements to numeric values.
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    for column in MEASUREMENT_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df["species"] = df["species"].astype("string").str.strip().str.lower()

    # Invalid measurement values and records without a species cannot be used.
    df = df.dropna(subset=REQUIRED_COLUMNS)
    df = df[df["species"].ne("")]
    rows_after_missing_values = len(df)
    df = df.drop_duplicates().reset_index(drop=True)

    # Data quality assertions: schema, types, nulls, and plausible measurements.
    assert list(df.columns) == REQUIRED_COLUMNS
    assert df[REQUIRED_COLUMNS].notna().all().all()
    assert all(pd.api.types.is_numeric_dtype(df[c]) for c in MEASUREMENT_COLUMNS)
    assert (df[MEASUREMENT_COLUMNS] > 0).all().all()
    assert set(df["species"].unique()) <= {"setosa", "versicolor", "virginica"}

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Source: {DATA_URL}")
    print(f"Rows downloaded: {rows_downloaded}")
    print(f"Rows after removing missing/invalid records: {rows_after_missing_values}")
    print(f"Rows after removing duplicates: {len(df)}")
    print(f"Output shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Output: {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")
    print("Species counts:")
    print(df["species"].value_counts().sort_index().to_string())
    print("Measurement summary:")
    print(df[MEASUREMENT_COLUMNS].describe().round(2).to_string())


if __name__ == "__main__":
    main()
