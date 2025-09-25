from app import app
def test_home():
    response = app.test_client().get('/')
    assert response.data == b'HELLO WORLD'
    assert response.status_code == 200