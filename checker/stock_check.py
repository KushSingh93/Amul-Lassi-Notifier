import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def is_in_stock(product_url: str) -> bool:
    response = requests.get(product_url, headers=HEADERS, timeout=15)
    if response.status_code != 200:
        return False

    html = response.text.lower()

    if "sold out" in html:
        return False
    if "notify me" in html:
        return False
    if "addtocart" in html or "add-to-cart" in html:
        return True

    return False
