
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "prices.csv"
ALERT_THRESHOLD = 5.0

df = pd.read_csv(DATA_FILE)

if df.empty:
    print("No price records available yet.")
    raise SystemExit

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["date", "price"])

for product, group in df.groupby("product_name"):
    history = (
        group.sort_values("date")
        .drop_duplicates(subset=["date"], keep="last")
    )

    print(f"\nProduct: {product}")

    if len(history) < 2:
        print("Not enough history to detect a price drop.")
        print("Record a price on another date to enable alerts.")
        continue

    previous_price = history.iloc[-2]["price"]
    latest_price = history.iloc[-1]["price"]

    if previous_price <= 0:
        print("Cannot calculate the price change.")
        continue

    change_percent = (
        (latest_price - previous_price) / previous_price
    ) * 100

    print(f"Previous price: ₹{previous_price:,.2f}")
    print(f"Latest price: ₹{latest_price:,.2f}")
    print(f"Price change: {change_percent:.2f}%")

    if change_percent <= -ALERT_THRESHOLD:
        print("PRICE DROP ALERT: Price decreased by 5% or more!")
    elif change_percent < 0:
        print("Price decreased, but by less than 5%.")
    else:
        print("No price-drop alert.")
