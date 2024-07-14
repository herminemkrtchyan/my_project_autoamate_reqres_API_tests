import requests
import pytest
import allure


@allure.feature("Test Delay - Feature")
@allure.suite('Test Delay - Suite')
class TestDelay:

    @allure.title("Verify Delayed Response Handling")
    @allure.description("Test to verify handling of delayed responses")
    @pytest.mark.regression
    def test_delayed_response(self):
        response = requests.get('https://reqres.in/api/users?delay=3')
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
        assert len(response.json()) != 0, 'Error, No data found'
