import requests
import pytest
import allure


@allure.feature('Test User Updates - Feature')
@allure.suite('Test User Updates - Suite')
class TestUpdatesAndDelete:

    @allure.title("Verify Update of User")
    @allure.description("Test to verify the update of a user")
    @pytest.mark.smoke
    def test_update_user(self):
        resource_id = 2
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'https://reqres.in/api/users/{resource_id}', json=data, headers=headers)
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'
        response_data = response.json()
        assert response_data['name'] == data['name'], f'Expected first name to be {data["name"]}, but got {response_data["name"]}'
        assert response_data['job'] == data['job'], f'Expected job to be {data["job"]}, but got {response_data["job"]}'
        assert len(response_data) != 0, f'Error, No data found'

    @allure.title("Verify Partial Update of User")
    @allure.description("Test to verify the partial update (PATCH) of a user by ID")
    @pytest.mark.regression
    def test_patch_update_user(self):
        resource_id = 2
        data = {
            "name": "boo"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(f'https://reqres.in/api/users/{resource_id}', json=data, headers=headers)
        assert response.status_code == 200, f'Expected status code 201, but got {response.status_code}'
        response_data = response.json()
        assert response_data['name'] == data['name'], f'Expected first name to be {data["name"]}, but got {response_data["name"]}'
        assert len(response_data) != 0, f'Error, No data found'

    @allure.title("Verify Deletion of User")
    @allure.description("Test to verify the deletion of a user")
    @pytest.mark.smoke
    def test_delete_user(self):
        resource_id = 2
        response = requests.delete(f'https://reqres.in/api/users/{resource_id}')
        assert response.status_code == 204, f'Expected status code 204, but got {response.status_code}'

