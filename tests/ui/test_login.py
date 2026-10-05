import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_valid(page):
    login = LoginPage(page)
    login.deschide()
    inventar = login.logheaza("standard_user", "secret_sauce")
    expect(inventar.titlu).to_have_text("Products")


@pytest.mark.regression
@pytest.mark.parametrize("user, parola, mesaj", [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("standard_user", "parola_gresita", "do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_login_invalid(page, user, parola, mesaj):
    login = LoginPage(page)
    login.deschide()
    login.logheaza(user, parola)
    expect(login.eroare).to_contain_text(mesaj)
