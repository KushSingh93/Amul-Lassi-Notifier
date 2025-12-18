# checker/stock_check.py

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def is_in_stock(product_url: str) -> bool:
    response = requests.get(product_url, headers=HEADERS, timeout=15)
    if response.status_code != 200:
        return False

    html = response.text.lower()

    # Single source of truth
    if "Sold Out" in html:
        return False

    return True
