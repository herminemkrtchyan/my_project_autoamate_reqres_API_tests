import requests
import pytest
import allure


@allure.feature("Test Registration and Login - Feature")
@allure.suite('Test Registration and Login - Suite')
class TestRegisterLogin:

    @allure.title("Verify Registration Functionality")
    @allure.description("Test to verify the registration functionality")
    @pytest.mark.smoke
    def test_register(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://reqres.in/api/register', json=data, headers=headers)
        response_data = response.json()
        assert response.status_code == 200, f'Expected status code {response.status_code}'
        assert response_data['token'] is not None

    @allure.title("[Negative] Verify Error Handling for Invalid Registration")
    @allure.description("Test to verify the error handling when attempting an invalid registration")
    @pytest.mark.regression
    def test_negative_register(self):
        data = {
            "email": "sydney@fife"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://reqres.in/api/register', json=data, headers=headers)
        assert response.status_code == 400, f'Expected Status Code 404, but got {response.status_code}'

    @allure.title("Verify Login Functionality")
    @allure.description("Test to verify the login functionality")
    @pytest.mark.smoke
    def test_login(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://reqres.in/api/login', json=data, headers=headers)
        response_data = response.json()
        assert response.status_code == 200, f'Expected status code {response.status_code}'
        assert response_data['token'] is not None

    @allure.title("[Negative] Verify Error Handling for Invalid Login ")
    @allure.description("Test to verify the error handling when attempting an invalid login")
    @pytest.mark.regression
    def test_negative_login(self):
        data = {
            "email": "peter@klaven"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://reqres.in/api/login', json=data, headers=headers)
        response_data = response.json()
        assert response.status_code == 400, f'Expected Status Code 404, but got {response.status_code}'
        assert response_data['error'] == "Missing password"
