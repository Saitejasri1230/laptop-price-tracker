# Laptop Price Tracker with Trend Analysis

A Python-based project that collects laptop prices from Dell Store India, records price history, analyzes price changes, generates visualizations, and checks for price drops.

## Project Overview

This project tracks the price of the Dell XPS 13 Laptop (2026) using its product page on Dell Store India. It stores price observations in a CSV file and generates summary reports and a price chart.

**Note:** The project currently has one real price observation. Price trends and price-drop alerts require observations from multiple dates.

## Features

- Collect laptop prices from a product page
- Store price records in CSV format
- Analyze recorded price history using Pandas
- Generate price summary reports
- Visualize recorded prices using Matplotlib
- Check for price drops of 5% or more
- Avoid duplicate records for the same product on the same date

## Technologies Used

- Python
- Requests
- Beautiful Soup
- Pandas
- Matplotlib
- CSV
- Git and GitHub

## Project Structure


laptop-price-tracker/
├── data/
│   ├── laptop_sample.csv
│   ├── prices.csv
│   └── products.csv
├── outputs/
│   ├── latest_laptop_prices.png
│   ├── price_history_analysis.csv
│   └── price_summary.csv
├── .gitignore
├── check_dell_access.py
├── collect_price.py
├── main.py
├── price_alert.py
├── requirements.txt
├── visualize.py
└── README.md


## Installation and Setup

### 1. Clone the repository


git clone https://github.com/Saitejasri1230/laptop-price-tracker.git
cd laptop-price-tracker


### 2. Create a virtual environment


python -m venv .venv


Activate it on Windows PowerShell:


.\.venv\Scripts\Activate.ps1


### 3. Install dependencies

pip install -r requirements.txt


## How to Run

Run the following commands from the project folder.

### Collect the latest price

python collect_price.py


### Analyze recorded prices


python main.py

### Generate the price chart


python visualize.py


### Check for price drops


python price_alert.py


The price alert checks whether the latest recorded price has dropped by at least 5% compared with the previous observation. It needs price records from different dates to calculate a meaningful change.

## Sample Recorded Price

| Field | Value |
|---|---|
| Product | Dell XPS 13 Laptop (2026) |
| Retailer | Dell Store India |
| Recorded price | ₹84,990 |
| Observation date | October 21, 2026 |

This is a historical observation recorded by the project, not a guarantee of the current selling price.

## Outputs

The project generates:

- `price_history_analysis.csv` — analysis of recorded price observations
- `price_summary.csv` — summary statistics for each tracked product
- `latest_laptop_prices.png` — visualization of recorded prices

## Future Improvements

- Track additional laptop models and retailers
- Collect observations automatically on a schedule
- Analyze price changes across longer periods
- Add email notifications for price drops
- Build an interactive dashboard

## Disclaimer

This project is intended for learning and portfolio demonstration. Website access and automated collection should follow the retailer's terms of service and applicable policies. Prices and product availability may change.

## Author

**Sai Tejasri Kotla**

GitHub: https://github.com/Saitejasri1230
