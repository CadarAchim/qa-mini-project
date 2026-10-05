import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def configureaza_test_id(playwright):
    # saucedemo folosește atributul "data-test", nu "data-testid"
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def inventar(page):
    # setup: utilizator deja logat, gata de test
    login = LoginPage(page)
    login.deschide()
    return login.logheaza("standard_user", "secret_sauce")
