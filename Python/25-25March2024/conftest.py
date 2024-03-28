import requests
import pytest

@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, json=payload, headers=headers)
    data = response.json()
    token = data["token"]
    print(token)
    return token

@pytest.fixture
def create_booking():
   base_url = "https://restful-booker.herokuapp.com"
   base_path = "/booking"
   URL = base_url + base_path
   headers = {
         'Content-Type': 'application/json'
    }
   payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
   response = requests.post(url=URL, json=payload, headers=headers)

   assert response.status_code == 200, "Test failed because status code is not 200"
   print(response.headers)
   data = response.json()
   booking_id = data["bookingid"]
   return booking_id