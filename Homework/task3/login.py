import requests

def test_login_user():

    url = 'https://petstore.swagger.io/v2'
    user_name = 'Boo'
    password = 'qwerty'

    login_user_request = requests.get(url=f"{url}/user/login", json={
    "username": user_name,
    "password": password
    })

    print(login_user_request.status_code)
    response = login_user_request.json()['message']

    assert login_user_request.status_code == 200, "User is not logged in"
    assert 'logged in user session:' in response
    
