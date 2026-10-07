# QA Mini Project – Pytest + Playwright + API

Test automation framework for UI and API testing, built with Python.

- **UI:** [saucedemo.com](https://www.saucedemo.com) – login and cart flows
- **API:** [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) – CRUD on `/posts`

## Tech stack
Python · Pytest · Playwright · requests · GitHub Actions

## Structure
```
pages/          Page Object Model (BasePage, LoginPage, InventoryPage)
tests/ui/       UI tests + fixtures (conftest.py)
tests/api/      API tests + session fixtures (conftest.py)
.github/        CI pipeline – runs on every push / pull request
```

## Key concepts
- Page Object Model, no assertions inside page objects
- Fixtures with different scopes (`session`, `function`), shared via `conftest.py`
- Data-driven negative tests with `@pytest.mark.parametrize`
- Markers: `smoke`, `regression`, `api`
- Traces and screenshots kept for failed tests

## Run locally
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install

pytest -v                       # all tests
pytest -m smoke -v              # smoke only
pytest -m api -v                # API only
pytest tests/ui --headed        # watch the browser
pytest --tracing retain-on-failure --screenshot only-on-failure
```
