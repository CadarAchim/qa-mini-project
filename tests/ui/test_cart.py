import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_adauga_produs_in_cos(inventar):
    inventar.adauga_in_cos("sauce-labs-backpack")
    expect(inventar.badge_cos).to_have_text("1")


@pytest.mark.regression
def test_adauga_doua_produse(inventar):
    inventar.adauga_in_cos("sauce-labs-backpack")
    inventar.adauga_in_cos("sauce-labs-bike-light")
    expect(inventar.badge_cos).to_have_text("2")


@pytest.mark.regression
def test_scoate_produs_din_cos(inventar):
    inventar.adauga_in_cos("sauce-labs-backpack")
    inventar.scoate_din_cos("sauce-labs-backpack")
    expect(inventar.badge_cos).to_be_hidden()
