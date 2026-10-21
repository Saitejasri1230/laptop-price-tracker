
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "prices.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
CHART_FILE = OUTPUT_DIR / "latest_laptop_prices.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)
df["date"] = pd.to_datetime(df["date"])
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["date", "price"])
df = df.sort_values("date")

if df.empty:
    raise ValueError("No valid price records found.")

plt.figure(figsize=(10, 6))

for product, group in df.groupby("product_name"):
    plt.plot(
        group["date"],
        group["price"],
        marker="o",
        label=product,
    )

plt.title("Recorded Laptop Price History")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig(CHART_FILE, dpi=150)
plt.close()

print("Price chart created successfully.")
print("Products plotted:", df["product_name"].nunique())
print("Price records:", len(df))
print("Chart saved to:", CHART_FILE)
print("Note: Trend analysis requires observations from different dates.")
