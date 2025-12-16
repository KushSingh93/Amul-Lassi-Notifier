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

    # Out of stock indicators (server-side)
    if "notify me" in html:
        return False

    if "add to cart" not in html:
        return False

    return True
