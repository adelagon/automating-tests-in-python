# coding=utf-8
"""users CRUD methods feature tests."""
import json
import pytest
import requests
import operator
from faker import Faker
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from conftest import Config, Storage

# Load scenarios from the feature file
scenarios('features/users_crud.feature')

@pytest.fixture(scope="module")
def values():
    """
    Generate random values
    """
    fake = Faker()
    yield {
        "name": fake.name(),
        "username": fake.email().split('@')[0],
        "email": fake.company_email(),
        "phone": fake.phone_number(),
        "website": fake.domain_name(),
        "address": {
            "street": fake.street_address(),
            "suite": fake.building_number(),
            "city": fake.city(),
            "zipcode": fake.postcode()
        },
        "company": {
            "name": fake.company(),
            "catchPhrase": fake.catch_phrase(),
            "bs": fake.bs()
        }
    }
    ### Cleanup

### This specific function is reused by multiple scenarios due to the parser match
@then(parsers.parse('the response status code is "{status:d}"'))
def the_response_status_code_is_(status):
    """
    This gets reused for every stratus code check
    """
    assert Storage.response.status_code == status

### Helper Function for sending requests
def send_request(method, endpoint, id=None, values=None):
    if id:
        endpoint = endpoint.format(id)
    if values:
        r = requests.request(
            method,
            endpoint,
            data=json.dumps(values),
            headers={'Content-Type': 'application/json'}
        )
    else:
        r = requests.request(
            method,
            endpoint,
        )
    Storage.response = r

### Scenario: Add User
@given(parsers.parse('the Users API is sent a random user profile using "{method}" method'))
def add_user(values, method):
    """
    It is important to note the {method} on the decorator. This allows to collect parameters from 
    the feature file. In this case, the HTTP method being used is dynamically injected by the
    feature file (in case you want to change HTTP methods)
    """
    send_request(method, Config.users_endpoint, id=Storage.user_id, values=values)

@then(parsers.parse('the response contains an "{required_field}" field'))
def the_response_contains_an_id_field(required_field):
    # Save User id for the next scenarios
    Storage.user_id = Storage.response.json()['id']
    assert required_field in Storage.response.json()

### Scenario: Update User
@given(parsers.parse('an existing user, I update its profile with a random "name" using "{method}" method'))
def update_user_response(values, method, faker):
    values['name'] = faker.name()
    send_request(method, Config.user_endpoint, id=Storage.user_id, values=values)

@then(parsers.parse('the response "{field}" field should be equal to the random name'))
def the_response_name_field_should_be_equal_to_the_random_name(values, field):
    assert Storage.response.json()[field] == values['name']

### Scenario: Get User
@given(parsers.parse('an existing user, I will get its profile using its "id" and "{method}" method'))
def get_user_response(method):
    send_request(method, Config.user_endpoint, id=Storage.user_id)

@then('the response body should be equal to the latest version of the profile after update')
def the_response_body_should_be_equal_to_the_latest_version_of_the_profile_after_update(values):
    values['id'] = Storage.response.json()['id']
    assert operator.eq(values, Storage.response.json()) == True

### Scenario: Delete User
@given(parsers.parse('an existing user, I will delete it using its "id" and "{method}" method'))
def delete_user_response(method):
    send_request(method, Config.user_endpoint, id=Storage.user_id)

@given(parsers.parse('the deleted user, I will attempt to get its profile using its "id" and "{method}" method'))
def get_deleted_user(method):
    send_request(method, Config.user_endpoint, id=Storage.user_id)

