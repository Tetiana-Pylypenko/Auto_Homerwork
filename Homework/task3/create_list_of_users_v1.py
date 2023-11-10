import requests
import pytest

def user_json(user_name):
    return {
    "id": 0,
    "username": user_name,
    "firstName": "FirstName",
    "lastName": "QATester",
    "email": "qatest@test.com",
    "password": "qwerty",
    "phone": "12345678",
    "userStatus": 0
    }

def test_create_list_of_users():

    url = 'https://petstore.swagger.io/v2'
    user_name1 = 'Alice'
    user_name2 = 'Bob'
    user_name3 = 'Jill'

    create_userlist_request = requests.post(url=f"{url}/user/createWithList", json=[user_json(user_name1), user_json(user_name2), user_json(user_name3)])
    print(create_userlist_request.status_code)
    print(create_userlist_request.json())

    assert requests.get(url=f"{url}/user/{user_name1}").status_code == 200
    assert requests.get(url=f"{url}/user/{user_name2}").status_code == 200
    assert requests.get(url=f"{url}/user/{user_name3}").status_code == 200
    
    
