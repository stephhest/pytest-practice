import pytest
import requests
import json

def test_login_valid(supply_url):
	url = supply_url + "/login/"
	data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
	res = requests.post(url, data=data)
	res_data = json.loads(res.text)
	assert res.status_code == 200, res.text
	assert res_data['token'] == "QpwL5tke4Pnpja7X4", res.text

def test_login_no_password(supply_url):
	url = supply_url + "/login/"
	data = {"email": "eve.holt@reqres.in"}
	res = requests.post(url, data=data)
	res_data = json.loads(res.text)
	assert res.status_code == 400, res.text
	assert res_data['error'] == "Missing password", res.text

def test_login_no_email(supply_url):
	url = supply_url + "/login/"
	data = {}
	res = requests.post(url, data=data)
	res_data = json.loads(res.text)
	assert res.status_code == 400, res.text
	assert res_data['error'] == "Missing email or username", res.text
