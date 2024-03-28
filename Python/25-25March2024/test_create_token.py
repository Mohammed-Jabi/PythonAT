import requests

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

def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking()
    PUT_URL = base_url + base_path + str(param)
    cookie = "token=" + create_token()
    headers = {
        'Content-Type': 'application/json',
        'Cookie': cookie
    }
    print(headers)
    json_payload = {
        "firstname": "Jabir",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, json=json_payload, headers=headers)
    assert response.status_code == 200, "Test failed because status code is not 200"
    assert response.json()["firstname"] == "Jabir", "Test failed because firstname is not updated"
    print(response.json())

def test_delete():
    try:
        URL = "https://restful-booker.herokuapp.com"
        booking_id = create_booking()
        DELETE_URL = URL + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {
            "Content-Type" : "application/json",
            "Cookie" : cookie_value
        }
        print(headers)
        response = requests.delete(url = DELETE_URL, headers=headers)
        assert response.status_code == 201
    except Exception as e:
        print(e)


