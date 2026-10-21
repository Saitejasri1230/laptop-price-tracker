
import requests
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path
import csv
import re

URL = "https://www.dellstore.com/xps-13-laptop-cdx13260cto02mino.html"
PRODUCT_NAME = "Dell XPS 13 Laptop (2026)"
RETAILER = "Dell Store India"

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "prices.csv"

response = requests.get(
    URL,
    timeout=20,
    headers={"User-Agent": "Mozilla/5.0"},
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(" ", strip=True)

match = re.search(
    r"₹\s*([\d,]+(?:\.\d{2})?)\s*Inclusive of all taxes",
    page_text,
)

if not match:
    raise ValueError("Price not found. No record was changed.")

price = float(match.group(1).replace(",", ""))
today = date.today().isoformat()

CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
fieldnames = [
    "date", "product_name", "retailer",
    "price", "currency", "product_url"
]

if CSV_FILE.exists():
    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
else:
    rows = []

new_record = {
    "date": today,
    "product_name": PRODUCT_NAME,
    "retailer": RETAILER,
    "price": f"{price:.2f}",
    "currency": "INR",
    "product_url": URL,
}

updated = False

for row in rows:
    if (
        row["date"] == today
        and row["product_name"] == PRODUCT_NAME
        and row["retailer"] == RETAILER
    ):
        row.update(new_record)
        updated = True
        break

if not updated:
    rows.append(new_record)

with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Price", "updated" if updated else "recorded", "successfully.")
print("Date:", today)
print("Product:", PRODUCT_NAME)
print(f"Price: ₹{price:,.2f}")
print("Total records:", len(rows))
print("Saved to:", CSV_FILE)
