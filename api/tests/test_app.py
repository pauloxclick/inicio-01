import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/auth/login', json={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected(client):
    response = client.get('/auth/protected')
    assert response.status_code == 401

    login_response = client.post('/auth/login', json={'username': 'admin', 'password': 'password'})
    token = login_response.json['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    protected_response = client.get('/auth/protected', headers=headers)
    assert protected_response.status_code == 200
    assert protected_response.json['msg'] == 'Access granted'