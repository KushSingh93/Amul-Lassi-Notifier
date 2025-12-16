from checker.products import PRODUCTS
from checker.stock_check import is_in_stock
from checker.pincode_check import is_pincode_serviceable
from checker.state_manager import load_state, save_state, get_transitions
import sys

def check_all():
    current = {}
    for key, product in PRODUCTS.items():
        stock_ok = is_in_stock(product["url"])
        pincode_ok = is_pincode_serviceable(product["url"])
        current[key] = stock_ok and pincode_ok

    return current


if __name__ == "__main__":
    previous = load_state()
    current = check_all()
    transitions = get_transitions(previous, current)

    for key, should_notify in transitions.items():
        if should_notify:
            product = PRODUCTS[key]
            print("🚨 PRODUCT AVAILABLE 🚨")
            print(product["name"])
            print(product["url"])

            # ✅ SAVE STATE FIRST
            save_state(current)

            # ✅ THEN fail to trigger GitHub notification
            sys.exit(1)

    # Normal path (no notification)
    save_state(current)
