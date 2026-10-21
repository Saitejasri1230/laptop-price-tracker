# import requests
# import bs4
# import pandas as pd
# import matplotlib.pyplot as plt

# print("All project libraries imported successfully!")
# print("Laptop Price Tracker setup is ready.")


# import pandas as pd

# file_path = "data/laptop_sample.csv"

# df = pd.read_csv(file_path)

# print("\n--- LAPTOP SAMPLE DATASET ---")
# print("\nFirst 5 rows:")
# print(df.head())

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nDataset size:")
# print(f"Rows: {df.shape[0]}")
# print(f"Columns: {df.shape[1]}")


# import pandas as pd

# file_path = "data/laptop_sample.csv"
# df = pd.read_csv(file_path)

# df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

# print("\n--- DATE RANGE ---")
# print("Earliest date:", df["Month"].min())
# print("Latest date:", df["Month"].max())

# print("\n--- LAPTOP MODELS ---")
# print(df["Model"].value_counts())

# print("\n--- PRICE SUMMARY ---")
# print(df["Price_Per_Unit_INR"].describe())

# print("\n--- MISSING VALUES ---")
# print(df.isnull().sum())

# print("\n--- DUPLICATE ROWS ---")
# print(df.duplicated().sum())


# import pandas as pd

# df = pd.read_csv("data/laptop_sample.csv")

# summary = df.groupby("Model")["Price_Per_Unit_INR"].agg(
#     Average_Price="mean",
#     Minimum_Price="min",
#     Maximum_Price="max"
# ).round(2)

# summary = summary.sort_values("Average_Price")

# print("\n--- PRICE COMPARISON BY LAPTOP MODEL ---")
# print(summary.to_string())

# summary.to_csv("data/model_price_summary.csv")

# print("\nSummary saved to data/model_price_summary.csv")


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("data/model_price_summary.csv")

# df = df.sort_values("Average_Price")

# plt.figure(figsize=(10, 6))
# plt.barh(df.index if df.index.name == "Model" else df["Model"],
#          df["Average_Price"])

# plt.title("Average Laptop Prices by Model")
# plt.xlabel("Average Price (INR)")
# plt.ylabel("Laptop Model")
# plt.tight_layout()

# plt.savefig("data/laptop_price_comparison.png", dpi=300)
# plt.show()

# print("Chart saved to data/laptop_price_comparison.png")


# import pandas as pd

# df = pd.read_csv("data/laptop_sample.csv")
# df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

# monthly_prices = df.groupby(
#     [pd.Grouper(key="Month", freq="ME"), "Model"]
# )["Price_Per_Unit_INR"].mean().reset_index()

# monthly_prices["Price_Per_Unit_INR"] = monthly_prices[
#     "Price_Per_Unit_INR"
# ].round(2)

# print("\n--- FIRST 15 MONTHLY PRICE RECORDS ---")
# print(monthly_prices.head(15).to_string(index=False))

# monthly_prices.to_csv("data/monthly_price_trends.csv", index=False)

# print("\nMonthly trend data saved to data/monthly_price_trends.csv")


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("data/monthly_price_trends.csv")
# df["Month"] = pd.to_datetime(df["Month"])

# plt.figure(figsize=(12, 7))

# for model in df["Model"].unique():
#     model_data = df[df["Model"] == model]
#     plt.plot(
#         model_data["Month"],
#         model_data["Price_Per_Unit_INR"],
#         label=model
#     )

# plt.title("Laptop Price Trends Over Time (Sample Data)")
# plt.xlabel("Date")
# plt.ylabel("Average Price (INR)")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()

# plt.savefig("data/laptop_price_trends.png", dpi=300)
# plt.show()

# print("Trend chart saved to data/laptop_price_trends.png")




# import pandas as pd

# df = pd.read_csv("data/price_changes.csv")

# price_drops = df.dropna(subset=["Price_Change_Percent"])

# price_drops = price_drops[
#     price_drops["Price_Change_Percent"] < 0
# ]

# top_drops = price_drops.sort_values(
#     "Price_Change_Percent"
# ).head(5)

# print("\n--- TOP 5 MONTHLY PRICE DROPS ---")

# print(
#     top_drops[
#         [
#             "Month",
#             "Model",
#             "Previous_Month_Price",
#             "Price_Per_Unit_INR",
#             "Price_Change_INR",
#             "Price_Change_Percent",
#         ]
#     ].to_string(index=False)
# )

# top_drops.to_csv("data/top_price_drops.csv", index=False)

# print("\nTop price drops saved to data/top_price_drops.csv")


# import pandas as pd

# df = pd.read_csv("data/price_changes.csv")

# ALERT_THRESHOLD_PERCENT = -5.0

# alerts = df[
#     df["Price_Change_Percent"] <= ALERT_THRESHOLD_PERCENT
# ].copy()

# alerts = alerts.sort_values("Price_Change_Percent")

# alerts["Alert"] = "PRICE DROP ALERT"

# print("\n--- PRICE DROP ALERTS ---")
# print(f"Alert threshold: {abs(ALERT_THRESHOLD_PERCENT)}% or greater decrease")

# if alerts.empty:
#     print("No price drops met the alert threshold.")
# else:
#     print(
#         alerts[
#             [
#                 "Month",
#                 "Model",
#                 "Previous_Month_Price",
#                 "Price_Per_Unit_INR",
#                 "Price_Change_Percent",
#                 "Alert",
#             ]
#         ].to_string(index=False)
#     )

# alerts.to_csv("data/price_drop_alerts.csv", index=False)

# print("\nAlerts saved to data/price_drop_alerts.csv")


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("data/monthly_price_trends.csv")
# df["Month"] = pd.to_datetime(df["Month"])

# latest_date = df["Month"].max()
# latest_prices = df[df["Month"] == latest_date].copy()
# latest_prices = latest_prices.sort_values("Price_Per_Unit_INR")

# plt.figure(figsize=(10, 6))

# plt.barh(
#     latest_prices["Model"],
#     latest_prices["Price_Per_Unit_INR"]
# )

# plt.title(f"Laptop Price Dashboard - {latest_date:%B %Y}")
# plt.xlabel("Average Price (INR)")
# plt.ylabel("Laptop Model")
# plt.tight_layout()

# plt.savefig("data/latest_laptop_prices.png", dpi=300)
# plt.show()

# print("\n--- LATEST SAMPLE PRICES ---")
# print(
#     latest_prices[["Model", "Price_Per_Unit_INR"]]
#     .to_string(index=False)
# )

# print("\nDashboard chart saved to data/latest_laptop_prices.png")


# import pandas as pd

# df = pd.read_csv("data/laptop_sample.csv")
# df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

# summary = df.groupby("Model").agg(
#     Average_Price=("Price_Per_Unit_INR", "mean"),
#     Minimum_Price=("Price_Per_Unit_INR", "min"),
#     Maximum_Price=("Price_Per_Unit_INR", "max"),
#     Average_Units_Sold=("Units_Sold", "mean"),
#     Records=("Price_Per_Unit_INR", "count")
# ).round(2)

# summary["Price_Range"] = (
#     summary["Maximum_Price"] - summary["Minimum_Price"]
# ).round(2)

# summary = summary.sort_values("Average_Price")

# summary.to_csv("data/project_summary_report.csv")

# print("\n--- PROJECT SUMMARY REPORT ---")
# print(summary.to_string())

# print("\nReport saved to data/project_summary_report.csv")


from pathlib import Path

import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent
PRICES_FILE = BASE_DIR / "data" / "prices.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load recorded price history
prices = pd.read_csv(PRICES_FILE)

# Validate required columns
required_columns = {
    "date",
    "product_name",
    "retailer",
    "price",
    "currency",
    "product_url",
}

missing_columns = required_columns - set(prices.columns)

if missing_columns:
    raise ValueError(f"Missing columns in prices.csv: {sorted(missing_columns)}")

# Clean and prepare data
prices["date"] = pd.to_datetime(prices["date"], errors="coerce")
prices["price"] = pd.to_numeric(prices["price"], errors="coerce")
prices = prices.dropna(subset=["date", "product_name", "price"])
prices = prices.sort_values(["product_name", "date"])

if prices.empty:
    raise ValueError("No valid price records found in data/prices.csv")

# Calculate changes between recorded prices
prices["previous_price"] = prices.groupby(
    ["product_name", "retailer", "currency"]
)["price"].shift(1)

prices["price_change"] = prices["price"] - prices["previous_price"]

prices["price_change_percent"] = (
    prices["price_change"] / prices["previous_price"] * 100
)

# Save the detailed history
history_file = OUTPUT_DIR / "price_history_analysis.csv"
prices.to_csv(history_file, index=False)

# Create a product summary
summary = (
    prices.groupby(["product_name", "retailer", "currency"], as_index=False)
    .agg(
        first_recorded_price=("price", "first"),
        latest_recorded_price=("price", "last"),
        lowest_recorded_price=("price", "min"),
        highest_recorded_price=("price", "max"),
        number_of_records=("price", "count"),
        latest_record_date=("date", "max"),
    )
)

summary["change_from_first_price_percent"] = (
    (summary["latest_recorded_price"] - summary["first_recorded_price"])
    / summary["first_recorded_price"]
    * 100
)

summary_file = OUTPUT_DIR / "price_summary.csv"
summary.to_csv(summary_file, index=False)

# Display results
print("\n--- RECORDED LAPTOP PRICE SUMMARY ---")
print(summary.to_string(index=False))

print(f"\nDetailed history saved to: {history_file}")
print(f"Price summary saved to: {summary_file}")

if (prices.groupby("product_name")["price"].count() < 2).all():
    print(
        "\nNote: Trend analysis needs at least two price records "
        "on different dates for a product."
    )
