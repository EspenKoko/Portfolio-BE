import sys
print("_____", sys.path)


import pytest
from app.services.user_services import getAllUsers
from app.models.user import User

def test_get_all_users_returns_json(memory_db):
    # Setup: add a user to the test database
    user = User(name="Test User", email="test@example.com")
    memory_db.session.add(user)
    memory_db.session.commit()

    # Act: call the service
    response = getAllUsers()

    # Assert: check response type and content
    assert response.status_code == 200
    data = response.get_json()
    assert any(u["email"] == "test@example.com" for u in data)
