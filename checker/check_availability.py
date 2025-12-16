# checker/check_availability.py

from checker.products import PRODUCTS
from checker.stock_check import is_in_stock
from checker.pincode_check import is_pincode_serviceable

def check_all():
    results = {}

    for key, product in PRODUCTS.items():
        stock_ok = is_in_stock(product["url"])
        pincode_ok = is_pincode_serviceable(product["url"])

        available = stock_ok and pincode_ok

        results[key] = {
            "stock": stock_ok,
            "pincode": pincode_ok,
            "available": available
        }

    return results


if __name__ == "__main__":
    results = check_all()
    for key, status in results.items():
        print(
            f"{key}: stock={status['stock']}, "
            f"pincode={status['pincode']}, "
            f"available={status['available']}"
        )