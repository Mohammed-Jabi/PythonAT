import pytest
import requests


@pytest.mark.smoke
def test_get_single_request_by_id():
   response =  requests.get("https://restful-booker.herokuapp.com/booking/1")
   response_status = response.status_code
   assert response_status == 200, "Test failed because status code is not 200"