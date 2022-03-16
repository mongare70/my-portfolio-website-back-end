from urllib import response
from app import app
with app.test_client() as c:
    response = c.get('/api')
    assert response.data == b'<h1>Test Success</h1>'
    assert response.status_code == 200