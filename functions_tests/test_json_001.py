import pytest
from functions.json import convert_dict_to_json, convert_json_to_dict
import json

# CONVERT DICT TO JSON
def test_convert_valid_dict_to_json():
    # Arrange
    input = {'name': 'John', 'age': 30}
    output = '{"name": "John", "age": 30}'
    # Act / Assert
    assert output == convert_dict_to_json(input)

# CONVERT JSON TO DICT
def test_convert_valid_json_to_dict():
    # Arrange
    input = '{"name": "John", "age": 30}'
    output = {'name': 'John', 'age': 30}
    # Act / Assert
    assert output == convert_json_to_dict(input)
