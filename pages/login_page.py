from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """Pagina de login: locatori + acțiuni, fără assert-uri."""

    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_test_id("username")
        self.parola = page.get_by_test_id("password")
        self.buton_login = page.get_by_test_id("login-button")
        self.eroare = page.get_by_test_id("error")

    def logheaza(self, user, parola):
        self.username.fill(user)
        self.parola.fill(parola)
        self.buton_login.click()
        return InventoryPage(self.page)
