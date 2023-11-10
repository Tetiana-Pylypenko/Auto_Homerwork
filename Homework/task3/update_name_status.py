import requests

def test_update_pet_name_status():
    url = 'https://petstore.swagger.io/v2'
    pet_name = "Rex"
    pet_status = "available"
    new_name = "Bob"
    new_status = "not availiable"

    pet_json = {
    "id": 11,
    "category": {
        "id": 0,
        "name": "Dogs"},
    "name": pet_name,
    "photoUrls": ["string"],
    "tags": [
        {
        "id": 0,
        "name": "doggi"
        }
    ],
    "status": pet_status
    }
    pet_json["name"] = pet_name
    pet_json["status"] = pet_status

    add_pet_request = requests.post(url=f"{url}/pet", json=pet_json)
    assert add_pet_request.status_code == 200

    pet_id = add_pet_request.json()['id']
    pet_json['id'] = pet_id
 
    pet_json["name"] = new_name
    pet_json["status"] = new_status
    
    update_pet_request = requests.put(url=f"{url}/pet", json=pet_json)
    assert update_pet_request.status_code == 200
    
    get_updated_pet = requests.get(url=f"{url}/pet/{pet_id}")
    
    updated_pet_name = get_updated_pet.json()['name']
    updated_pet_status = get_updated_pet.json()['status']

    assert pet_name != updated_pet_name, "Pet name is not updated"
    assert pet_status != updated_pet_status, "Pet status is not updated"