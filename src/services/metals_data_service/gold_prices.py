import requests
from src.utils import get_envar

def fetch_gold_price():
    api_key = get_envar("GOLDAPIIO_KEY")
    symbol = "XAU"
    curr = "USD"
    date = ""
    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}" 
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.text
        print(result)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))