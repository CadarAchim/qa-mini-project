import pytest
import requests


@pytest.fixture(scope="session")
def base_api():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api():
    # o singură sesiune HTTP refolosită de toate testele API
    sesiune = requests.Session()
    yield sesiune
    sesiune.close()
