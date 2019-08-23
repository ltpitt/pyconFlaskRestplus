"""test module for course1_solution.py"""

import pytest
import json
from flask import jsonify


from solutions import course4_solution


@pytest.fixture
def test_client():
    """configure app and get client for testing"""
    course4_solution.app.config['TESTING'] = True
    client = course4_solution.app.test_client()
    yield client


def test_post_employee(test_client):
    """test for posting an employeesk"""

    url = '/employee/5'
    data = {'Name': 'Test Post', 'Employee ID': 5}
    response = test_client.post(url, json=data)
    assert response.status_code == 200


def test_get_employee(test_client):
    """test for retrieving an employee"""

    url = '/employee/5'
    data = {'Employee ID': '5', 'Name': 'Test Post'}
    response = test_client.get(url)
    assert response.status_code == 200
    print(response.json)
    print(data)
    assert response.json == data


def test_put_employee(test_client):
    """test for modifying an employee"""

    url = '/employee/5'
    data = {'Name': 'Modified name', 'Employee ID': '5'}
    response = test_client.put(url, json=data)
    assert response.status_code == 200


def test_delete_employee(test_client):
    url = 'employee/5'
    response = test_client.delete(url)
    assert response.status_code == 200


