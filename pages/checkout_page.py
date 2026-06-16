class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.checkout_button = "#checkout"
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"

    def checkout(self, first_name, last_name, postal_code):
        self.page.click(self.checkout_button)

        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.postal_code, postal_code)

        self.page.click(self.continue_button)

    def finish_order(self):
        self.page.click(self.finish_button)
        
        self.page.wait_for_timeout(3000)