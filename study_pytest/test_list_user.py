import pytest
import requests
import json

# Tests for valid user fetch and verifies the res
@pytest.mark.parametrize("userid, firstname",[(7, "Michael"), (8, "Lindsay")])
def test_list_valid_user(supply_url, userid, firstname):
	url = supply_url + "/users/" + str(userid)
	res = requests.get(url)
	res_data = json.loads(res.text)
	assert res.status_code == 200, res.text
	assert res_data['data']['id'] == userid, res.text
	assert res_data['data']['first_name'] == firstname, res.text

# Tests for invalid user fetch and verifies the res
def test_list_invaliduser(supply_url):
	url = supply_url + "/users/50"
	res = requests.get(url)
	assert res.status_code == 404, res.text
