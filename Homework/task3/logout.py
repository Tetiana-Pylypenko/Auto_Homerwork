import requests

def test_logout_user():

    url = 'https://petstore.swagger.io/v2'
    user_name = 'Boo'
    password = 'qwerty'
    login_user_request = requests.get(url=f"{url}/user/login", json={
    "username": user_name,
    "password": password
    })
    print(login_user_request.status_code)

    logout_user_request = requests.get(url=f"{url}/user/logout")

    print(logout_user_request.status_code)
    print(logout_user_request.json())

    assert logout_user_request.status_code == 200, "User is not logged out"