import pytest
from functions.requests import create_something

def test_create_valid_something():
    # Arrange
    input = { "key": "value" }
    output = { "status_code": 200, "message": "success" }
    response = output.json()
    # Act / Assert
    assert response == create_something(input)
