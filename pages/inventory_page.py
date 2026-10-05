from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Pagina cu produse, pe care ajungi după login."""

    def __init__(self, page):
        super().__init__(page)
        self.titlu = page.get_by_test_id("title")
        self.badge_cos = page.get_by_test_id("shopping-cart-badge")

    def adauga_in_cos(self, produs):
        self.page.get_by_test_id(f"add-to-cart-{produs}").click()

    def scoate_din_cos(self, produs):
        self.page.get_by_test_id(f"remove-{produs}").click()
