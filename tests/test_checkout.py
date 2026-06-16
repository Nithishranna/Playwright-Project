from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.json_reader import read_json


def test_complete_checkout(page):

    login_data = read_json(
        "test_data/login_data.json"
    )

    checkout_data = read_json(
        "test_data/checkout_data.json"
    )

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    assert (
        cart_page.get_cart_item_name()
        == "Sauce Labs Backpack"
    )

    checkout_page.checkout(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )

    checkout_page.finish_order()

    assert "checkout-complete" in page.url