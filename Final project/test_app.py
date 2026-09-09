import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.get_db_connection')
def test_get_users(mock_db, client):
    mock_conn = mock_db.return_value
    mock_cursor = mock_conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [{"id": 1, "name": "Test User", "email": "test@example.com"}]
    
    response = client.get('/users')
    
    assert response.status_code == 200
    assert b"Test User" in response.data

@patch('app.get_db_connection')
def test_add_user_missing_data(mock_db, client):
    response = client.post('/users', json={"name": "Only Name"})
    assert response.status_code == 400
    assert b"Missing" in response.data