import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_citeste_post(api, base_api):
    r = api.get(f"{base_api}/posts/1", timeout=10)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert isinstance(body["title"], str)
    assert isinstance(body["userId"], int)


@pytest.mark.api
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_posturi_existente(api, base_api, post_id):
    r = api.get(f"{base_api}/posts/{post_id}", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == post_id


@pytest.mark.api
def test_post_inexistent(api, base_api):
    r = api.get(f"{base_api}/posts/99999", timeout=10)
    assert r.status_code == 404


@pytest.mark.api
def test_lista_posturi(api, base_api):
    r = api.get(f"{base_api}/posts", timeout=10)
    assert r.status_code == 200
    assert len(r.json()) == 100


@pytest.mark.api
def test_creeaza_post(api, base_api):
    date = {"title": "Test QA", "body": "Continut", "userId": 1}
    r = api.post(f"{base_api}/posts", json=date, timeout=10)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "Test QA"
    assert "id" in body


@pytest.mark.api
def test_actualizeaza_post(api, base_api):
    date = {"id": 1, "title": "Titlu nou", "body": "Text", "userId": 1}
    r = api.put(f"{base_api}/posts/1", json=date, timeout=10)
    assert r.status_code == 200
    assert r.json()["title"] == "Titlu nou"


@pytest.mark.api
def test_sterge_post(api, base_api):
    r = api.delete(f"{base_api}/posts/1", timeout=10)
    assert r.status_code == 200
