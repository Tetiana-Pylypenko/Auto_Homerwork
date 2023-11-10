import requests

def test_create_user():

    url = 'https://petstore.swagger.io/v2'
    user_name = 'Boom'

    create_user_request = requests.post(url=f"{url}/user", json={
    "id": 0,
    "username": user_name,
    "firstName": "Tetiana",
    "lastName": "QATester",
    "email": "qatest@test.com",
    "password": "qwerty",
    "phone": "12345678",
    "userStatus": 0
    })
    
    assert create_user_request.status_code ==200
    print(create_user_request.status_code)
    print(create_user_request.json())

    get_user = requests.get(url=f"{url}/user/{user_name}")
    actual_user_name = get_user.json()['username']
    
    assert actual_user_name == user_name, "User is not created"

