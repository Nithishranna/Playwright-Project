class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.backpack_add_to_cart = "#add-to-cart-sauce-labs-backpack"
        self.shopping_cart = ".shopping_cart_link"

    def add_backpack_to_cart(self):
        self.page.click(self.backpack_add_to_cart)

    def open_cart(self):
        self.page.click(self.shopping_cart)
        
        self.page.wait_for_timeout(3000)
