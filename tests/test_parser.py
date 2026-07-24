from app import app
client = app.test_client()
def test_valid_url():
    response = client.post(
        "/analyze",
        json={"url": "https://example.com"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "title" in data
    assert "status" in data
def test_invalid_url():
    response = client.post(
        "/analyze",
        json={"url": "hello"}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
def test_non_html_url():
    response = client.post(
        "/analyze",
        json={
            "url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data