
import requests

def test_create_users_with_list():
    # Define the API endpoint
    url = 'https://petstore.swagger.io/v2'

    # Create a list of user data
    users = [
        {
            "id": 0,
            "username": "user1",
            "firstName": "FirstName1",
            "lastName": "QATester1",
            "email": "user1@example.com",
            "password": "password1",
            "phone": "12345678",
            "userStatus": 0
        },
        {
            "id": 0,
            "username": "user2",
            "firstName": "FirstName2",
            "lastName": "QATester2",
            "email": "user2@example.com",
            "password": "password2",
            "phone": "23456789",
            "userStatus": 1
        },
        {
            "id": 0,
            "username": "user3",
            "firstName": "FirstName3",
            "lastName": "QATester3",
            "email": "user3@example.com",
            "password": "password3",
            "phone": "34567890",
            "userStatus": 2
        }
    ]

    response = requests.post(url=f"{url}/user/createWithArray", json=users)
    assert response.status_code == 200, "User list is not created"

    response_data = response.json()["message"]
    assert "ok" in response_data
    
