import pytest
import allure
import requests


@allure.title("Create Booking CURD")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive():
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
   response_json = response.json()#["bookingid"]
   booking_id = response_json["bookingid"]
   assert  booking_id is not None
   assert booking_id > 0
   assert type(booking_id) == int


@allure.title("Create Booking CURD")
@allure.description("TC#2 - Verify the create Booking is not created with{} data")
@pytest.mark.crud
@pytest.mark.negetive
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {
        'Content-Type': 'application/json'
    }
    payload = { }
    response = requests.post(url=URL, json=payload, headers=headers)
    print(type(URL))
    print(type(headers))
    print(type(payload))
    assert response.status_code == 500, "Test failed because status code is not 200"


