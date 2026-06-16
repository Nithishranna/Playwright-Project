from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.json_reader import read_json


def test_add_product_to_cart(page):
    data = read_json("test_data/login_data.json")

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()

    login_page.login(
        data["username"],
        data["password"]
    )

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    assert (
        cart_page.get_cart_item_name()
        == "Sauce Labs Backpack"
    )