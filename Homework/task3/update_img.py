import requests

def test_update_pet_img():
    url = 'https://petstore.swagger.io/v2'
    img_url = 'https://www.pexels.com/photo/close-up-photo-of-siberian-husky-6530642/'
    new_img_url = 'https://www.pexels.com/photo/white-and-black-siberian-husky-6530643/'

    pet_json = {
    "id": 100,
    "category": {
        "id": 0,
        "name": "Dogs"},
    "name": "Rex",
    "photoUrls": [],
    "tags": [
        {
        "id": 0,
        "name": "doggi"
        }
    ],
    "status": "available"
    }
    pet_json["photoUrls"] = [img_url]

    add_pet_request = requests.post(url=f"{url}/pet", json=pet_json)

    assert add_pet_request.status_code == 200
    pet_id = add_pet_request.json()['id']

    pet_json["photoUrls"] = [new_img_url]
    pet_json["id"] = pet_id

    update_pet_request = requests.put(url=f"{url}/pet", json=pet_json)
    assert update_pet_request.status_code == 200
    
    get_pet = requests.get(url=f"{url}/pet/{pet_id}")
    actual_pet = get_pet.json()['photoUrls'][0]

    assert actual_pet == new_img_url, "Image is not updated"
