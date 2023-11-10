import requests

def test_adding_new_pat():

    url = 'https://petstore.swagger.io/v2'

    add_new_pet_request = requests.post(url=f"{url}/pet", json={
    "id": 11,
    "category": {
        "id": 0,
        "name": "Dogs"},
    "name": "Rex",
    "photoUrls": [ "string"],
    "tags": [
        {
        "id": 0,
        "name": "doggi"
        }
    ],
    "status": "available"
    })

    assert add_new_pet_request.status_code == 200
    print(add_new_pet_request.status_code)
    print(add_new_pet_request.json())
    
    pet_id = add_new_pet_request.json()['id']
    get_pet = requests.get(url=f"{url}/pet/{pet_id}")
    actual_pet_id = get_pet.json()['id']
    
    assert actual_pet_id == pet_id, "Pet is not added"