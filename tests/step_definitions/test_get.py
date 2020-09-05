import pytest
import requests
from pytest_bdd import given, parsers, then, scenarios

scenarios('get.feature', strict_gherkin=False)


@given(parsers.parse('I make a GET request to "{url}"'))
def send_get_request(url):
    response = requests.get(url=url)
    pytest.globalDict['status_code'] = response.status_code


@then(parsers.parse('I expect response status code to be "{status_code}"'))
def validate_response(status_code):
    assert pytest.globalDict['status_code'] == int(status_code)
    print("Test Completed")
