# Laptop Price Tracker with Trend Analysis

A Python-based data analysis project that collects laptop prices from Dell Store India, records price observations, analyzes price history, generates visualizations, and checks for price drops. The project also includes a separate analysis of 14,000 synthetic laptop records to demonstrate data cleaning, aggregation, and trend analysis.

## Project Overview

This project combines two parts:

1. **Real Price Tracking:** Collects and stores a price observation for the Dell XPS 13 Laptop (2026) from Dell Store India.
2. **Sample Data Analysis:** Analyzes 14,000 synthetic laptop records across seven laptop models and 29 states to explore price distributions, sales patterns, and trends over time.

**Data limitation:** The real price tracker currently has only one recorded observation. Real price trends and price-drop alerts require observations collected on multiple dates. The 14,000-row dataset is synthetic and is used separately for analytical demonstrations, not as verified market data.

## Features

- Collect laptop prices from a product page
- Store price observations in CSV format
- Prevent duplicate records for the same product on the same date
- Analyze price history using Pandas
- Calculate average, minimum, and maximum prices by laptop model
- Summarize units sold by model and prices by state
- Generate CSV reports and visualizations
- Check for price drops of 5% or more
- Perform data cleaning and basic data-quality analysis
- Analyze 14,000 synthetic records across seven models and 29 states

## Technologies Used

- Python
- Pandas and NumPy
- Requests
- Beautiful Soup
- Matplotlib
- CSV
- Git and GitHub

## Project Structure

```text
laptop-price-tracker/
├── data/
│   ├── laptop_sample.csv
│   ├── prices.csv
│   └── products.csv
├── outputs/
│   ├── latest_laptop_prices.png
│   ├── price_history_analysis.csv
│   ├── price_summary.csv
│   ├── sample_data_quality.csv
│   ├── sample_model_price_summary.csv
│   ├── sample_model_sales_summary.csv
│   ├── sample_state_price_summary.csv
│   ├── sample_model_price_comparison.png
│   └── sample_price_over_time.png
├── .gitignore
├── analyze_sample_data.py
├── check_dell_access.py
├── collect_price.py
├── main.py
├── price_alert.py
├── requirements.txt
├── visualize.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Saitejasri1230/laptop-price-tracker.git
cd laptop-price-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Run these commands from the project folder.

### Collect a laptop price

```bash
python collect_price.py
```

### Analyze recorded price observations

```bash
python main.py
```

### Generate the recorded-price chart

```bash
python visualize.py
```

### Check for price drops

```bash
python price_alert.py
```

The alert script checks whether the latest recorded price has decreased by at least 5% compared with the previous observation. Multiple observations from different dates are required for a meaningful comparison.

### Analyze the 14,000-row sample dataset

```bash
python analyze_sample_data.py
```

This script cleans and analyzes the sample dataset and generates summary CSV files and charts in the `outputs/` directory.

## Sample Data Analysis

The sample analysis uses `data/laptop_sample.csv`.

| Analysis | Result |
|---|---|
| Total records analyzed | 14,000 |
| Laptop models | 7 |
| States represented | 29 |
| Data date range | January 2015 – June 2020 |

### Average price by laptop model

| Laptop model | Average price (INR) |
|---|---:|
| Precision 5570 | ₹199,900.01 |
| XPS 15 | ₹150,000.36 |
| XPS 13 | ₹123,445.48 |
| Gaming G15 | ₹97,632.16 |
| Latitude 14 | ₹79,777.65 |
| Vostro 14 | ₹52,088.79 |
| Inspiron 15 | ₹44,972.74 |

These figures describe the synthetic sample dataset and should not be interpreted as verified historical or current retail prices.

### Generated sample analysis outputs

- `sample_data_quality.csv` — data-quality summary
- `sample_model_price_summary.csv` — price statistics by laptop model
- `sample_model_sales_summary.csv` — units sold summarized by model
- `sample_state_price_summary.csv` — price summary by state
- `sample_model_price_comparison.png` — visual comparison of model prices
- `sample_price_over_time.png` — price trends across the sample period

## Sample Recorded Real-Price Observation

| Field | Value |
|---|---|
| Product | Dell XPS 13 Laptop (2026) |
| Retailer | Dell Store India |
| Recorded price | ₹84,990 |
| Observation date | October 21, 2026 |

This is a historical observation recorded by the project, not a guarantee of the current selling price.

## Future Improvements

- Track additional laptop models and retailers
- Schedule automated price collection
- Build a longer-term real price history
- Add email notifications for price drops
- Develop an interactive dashboard
- Expand data-quality checks and analysis

## Disclaimer

This project is intended for learning and portfolio demonstration. The sample dataset contains synthetic data, while the real-price tracker currently contains a limited number of actual observations. Website access and automated collection should comply with retailer terms of service and applicable policies. Prices and product availability may change.

## Author

**Sai Tejasri Kotla**

GitHub: https://github.com/Saitejasri1230
