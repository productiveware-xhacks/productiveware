import requests
from productiveware import config

base_url = "http://productiveware.objectobject.ca:3000"
login_url = f"{base_url}/api/auth/login"

def get_headers():
	return {
		"Cookie": f"connect.sid={config.get_cookie()}"
	}

def login(username, password):
	response = requests.post(login_url, json={"username": username, "password": password})
	if response.status_code != 200:
		return False
	config.set_cookie(response.cookies.get("connect.sid"))
	return True

def check_cookie():
	response = requests.get(f"{base_url}/api/todos", headers=get_headers())
	return response.status_code == 200

def get_encryption_key(cookie):
	"""Get the user's encryption key from the server."""
	return b"WkgJfErD7J_LqwX_hmAiFZfmVLOt1p7ZXpaCl0vdZgY=" # placeholder

requests.get(f"{base_url}/api/todos", headers=get_headers())