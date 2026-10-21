
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "laptop_sample.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load sample dataset
df = pd.read_csv(DATA_FILE)

# Clean column names and data types
df.columns = df.columns.str.strip()
df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

numeric_columns = [
    "Price_Per_Unit_INR",
    "GNP_INR",
    "Import_Duties_INR",
    "Units_Sold",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(
    subset=["Month", "State", "Model", "Price_Per_Unit_INR", "Units_Sold"]
)

# Save dataset quality report
quality_report = pd.DataFrame({
    "Metric": [
        "Rows after cleaning",
        "Number of laptop models",
        "Number of states",
        "Earliest sample date",
        "Latest sample date",
        "Missing values remaining",
    ],
    "Value": [
        len(df),
        df["Model"].nunique(),
        df["State"].nunique(),
        str(df["Month"].min().date()),
        str(df["Month"].max().date()),
        int(df.isna().sum().sum()),
    ],
})
quality_report.to_csv(OUTPUT_DIR / "sample_data_quality.csv", index=False)

# 1. Compare average prices by model
model_summary = (
    df.groupby("Model")["Price_Per_Unit_INR"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
    .rename(columns={
        "count": "Record_Count",
        "mean": "Average_Price_INR",
        "min": "Minimum_Price_INR",
        "max": "Maximum_Price_INR",
    })
    .sort_values("Average_Price_INR", ascending=False)
)
model_summary.to_csv(OUTPUT_DIR / "sample_model_price_summary.csv")

# 2. Compare units sold by model
sales_summary = (
    df.groupby("Model")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
    .rename("Total_Units_Sold")
    .reset_index()
)
sales_summary.to_csv(OUTPUT_DIR / "sample_model_sales_summary.csv", index=False)

# 3. Compare average prices by state
state_summary = (
    df.groupby("State")["Price_Per_Unit_INR"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .rename("Average_Price_INR")
    .reset_index()
)
state_summary.to_csv(OUTPUT_DIR / "sample_state_price_summary.csv", index=False)

# 4. Create a model price comparison chart
plt.figure(figsize=(11, 6))
model_summary["Average_Price_INR"].sort_values().plot(kind="barh")
plt.title("Average Laptop Price by Model (Sample Dataset)")
plt.xlabel("Average price (INR)")
plt.ylabel("Laptop model")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sample_model_price_comparison.png", dpi=150)
plt.close()

# 5. Create a daily average price chart
daily_prices = (
    df.groupby("Month")["Price_Per_Unit_INR"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(daily_prices.index, daily_prices.values)
plt.title("Recorded Sample Prices Over Time (Synthetic Dataset)")
plt.xlabel("Sample date")
plt.ylabel("Average price (INR)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sample_price_over_time.png", dpi=150)
plt.close()

# Display results
print("SAMPLE DATA ANALYSIS COMPLETED")
print("--------------------------------")
print(f"Rows analyzed: {len(df):,}")
print(f"Laptop models: {df['Model'].nunique()}")
print(f"States: {df['State'].nunique()}")
print(f"Date range: {df['Month'].min().date()} to {df['Month'].max().date()}")

print("\nAVERAGE PRICE BY MODEL")
print(model_summary.to_string())

print("\nTOP 5 MODELS BY TOTAL UNITS SOLD")
print(sales_summary.head(5).to_string(index=False))

print("\nNote: These are synthetic sample data, not verified market prices.")
print(f"\nReports and charts saved in: {OUTPUT_DIR}")
