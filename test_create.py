import requests
import pytest
import allure


@allure.feature("Test User Creation - Feature")
@allure.suite("Test User Creation - Suite")
class TestCreateUser:

    @allure.title("Verify Creation of User")
    @allure.description("Test to verify the creation of a user")
    @pytest.mark.smoke
    def test_create_user(self):
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/users', json=data, headers=headers)
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'
        response_data = response.json()
        assert response_data['name'] == data[
            'name'], f'Expected first name to be {data["name"]}, but got {response_data["name"]}'
        assert response_data['job'] == data['job'], f'Expected job to be {data["job"]}, but got {response_data["job"]}'
        assert len(response_data) != 0, f'Error, No data found'
        assert len(response_data['id']) != 0, f'Error, No data found'
        assert len(response_data['createdAt']) != 0, f'Error, No data found'
