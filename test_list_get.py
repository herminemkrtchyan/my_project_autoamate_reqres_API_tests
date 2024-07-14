import requests
import pytest
import allure


@allure.feature("Test List Get - Feature")
@allure.suite('Test List Get - Suite')
class TestListByGet:

    @allure.title("Verify Retrieval of Users List")
    @allure.description("Test to verify the successful retrieval of a list of users")
    @pytest.mark.smoke
    def test_get_users_list(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'
        assert len(response.json()) != 0, 'Error, No data found'

    @allure.title("Verify Retrieval of User by ID")
    @allure.description("Test to verify the retrieval of a single user by ID")
    @pytest.mark.smoke
    def test_get_user_by_id(self):
        user_id = 2
        response = requests.get(f'https://reqres.in/api/users/{user_id}')
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'
        assert len(response.json()) != 0, 'Error, No data found'

    @allure.title("[Negative] Verify Retrieval of Users for Non-existent User ID")
    @allure.description("Test to verify the error handling when retrieving a user by a non-existent ID")
    @pytest.mark.regression
    def test_negative_get_user_by_id(self):
        user_id = 23
        response = requests.get(f'https://reqres.in/api/users/{user_id}')
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'
        assert len(response.json()) == 0, 'User Not found'

    @allure.title("Verify Retrieval of User Resource List")
    @allure.description("Test to verify the retrieval of a user resource list")
    @pytest.mark.smoke
    def test_user_resource_list(self):
        response = requests.get('https://reqres.in/api/unknown')
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'
        assert len(response.json()) != 0, 'Error, No data found'

    @allure.title("Verify Retrieval of User Resource by ID")
    @allure.description("Test to verify the retrieval of a user resource by ID")
    @pytest.mark.smoke
    def test_user_resource_by_id(self):
        resource_id = 2
        response = requests.get(f'https://reqres.in/api/users/{resource_id}')
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'
        assert len(response.json()) != 0, 'Error, No data found'

    @allure.title("[Negative] Verify Retrieval of User Resource for Non-existent User ID")
    @allure.description("Test to verify the error handling when retrieving a user by a non-existent ID")
    @pytest.mark.regression
    def test_negative_user_resource_by_id(self):
        resource_id = 23
        response = requests.get(f'https://reqres.in/api/users/{resource_id}')
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'
        assert len(response.json()) == 0, 'User Not found'