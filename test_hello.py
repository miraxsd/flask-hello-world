import pytest
from flask import Flask, jsonify
from hello import app, make_me_laugh

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_make_me_laugh(client):
    response = client.get('/laugh')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert 'success' in data
    assert 'message' in data or isinstance(data.get('joke'), str)

def test_make_me_laugh_empty_jokes(client):
    # Temporarily modify the jokes list to be empty for testing
    original_jokes = make_me_laugh.__globals__['jokes']
    make_me_laugh.__globals__['jokes'] = []
    
    response = client.get('/laugh')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is False
    assert data['message'] == 'No jokes available.'

    # Restore the original jokes list
    make_me_laugh.__globals__['jokes'] = original_jokes