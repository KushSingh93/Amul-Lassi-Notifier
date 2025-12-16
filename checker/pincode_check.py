# checker/pincode_check.py

import requests

PINCODE = "110017"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def is_pincode_serviceable(product_url: str) -> bool:
    """
    Returns True if product is deliverable to PINCODE.
    Uses server-rendered signals instead of JS/localStorage.
    """

    cookies = {
        "pincode": PINCODE
    }

    try:
        response = requests.get(
            product_url,
            headers=HEADERS,
            cookies=cookies,
            timeout=15
        )
    except requests.RequestException:
        return False

    if response.status_code != 200:
        return False

    html = response.text.lower()

    # Strong negative indicators
    non_serviceable_markers = [
        "not deliverable",
        "delivery not available",
        "not serviceable"
    ]

    for marker in non_serviceable_markers:
        if marker in html:
            return False

    return True
