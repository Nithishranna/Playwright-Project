class CartPage:
    
    def __init__(self, page):
        self.page = page
        
        self.cart_item = ".inventory_item_name"
        
    def get_cart_item_name(self):
        return self.page.locator(self.cart_item).text_content()
        
        self.page.wait_for_timeout(3000)