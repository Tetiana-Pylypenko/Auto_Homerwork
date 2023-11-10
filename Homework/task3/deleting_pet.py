import requests

def test_deleting_pett():

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
    pet_id = add_new_pet_request.json()["id"]
  
    get_pet = requests.get(url=f"{url}/pet/{pet_id}")
    assert get_pet.status_code == 200

    delete_pet_request = requests.delete(url=f"{url}/pet/{pet_id}")
    assert delete_pet_request.status_code == 200

    get_pet = requests.get(url=f"{url}/pet/{pet_id}")
    assert get_pet.status_code == 404



