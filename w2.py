import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_daily_rate(currency_code, query_date):
    api_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    params = {
        "valcode": currency_code,
        "date": query_date,
        "json": ""
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data[0]["rate"] if data else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {query_date}: {e}")
        return None
def generate_date_range(days_count):
    today = datetime.now()
    return [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(days_count)]
def format_dates_for_plot(days_count):
    today = datetime.now()
    return [(today - timedelta(days=i)).strftime("%d.%m") for i in reversed(range(days_count))]
currency = "EUR"
num_days = 7
date_list = generate_date_range(num_days)
plot_dates = format_dates_for_plot(num_days)
exchange_rates = [fetch_daily_rate(currency, date) for date in reversed(date_list)]
plt.figure(figsize=(10, 6))
plt.plot(
    plot_dates,
    exchange_rates,
    marker="o",
    linestyle="-",
    color="blue",
    label=f"Exchange Rate: {currency}"
)
plt.title(f"Exchange Rate Trend for {currency} (Last {num_days} Days)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Rate (UAH)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()