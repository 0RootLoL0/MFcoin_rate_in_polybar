import requests
import json
import sys
import time

URL_MFC= "https://api.coingecko.com/api/v3/coins/mfcoin"

try:
    sys.stdout.write("MFC: " + str(requests.get(URL_MFC).json()["market_data"]["current_price"]["rub"]) + "P")
except requests.exceptions.ConnectionError:
    time.sleep(15)
