import requests
from bs4 import BeautifulSoup

usd_url = "https://bank.gov.ua/ua/markets/exchangerates"
response = requests.get(usd_url)
soup = BeautifulSoup(response.text, "html.parser")
usd_rate_tag = soup.find("td", {"data-label": "Офіційний курс"})

if usd_rate_tag:
    print(f"Долар США: {usd_rate_tag.text.strip()} грн")
