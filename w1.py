import requests
import json
from datetime import date, timedelta

def fetch_exchange_rates(currency_code, start_date, end_date):
    base_url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    query_params = {
        "start": start_date,
        "end": end_date,
        "valcode": currency_code,
        "sort": "exchangedate",
        "order": "desc",
        "json": ""
    }
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
def format_date(input_date):
    return input_date.strftime('%Y%m%d')
end_date = date.today()
start_date = end_date - timedelta(days=7)
start_date_str = format_date(start_date)
end_date_str = format_date(end_date)
currency = "USD"
exchange_rates = fetch_exchange_rates(currency, start_date_str, end_date_str)
if exchange_rates:
    print(f"Exchange rates for {currency} (Last 7 days):")
    for rate_entry in exchange_rates:
        print(f"Date: {rate_entry['exchangedate']}, Rate: {rate_entry['rate']}")
else:
    print(f"No exchange rates found for {currency}.")