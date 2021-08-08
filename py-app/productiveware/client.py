from . import encryption
import socketio
import requests
from urllib import parse
import re

base_url = "http://productiveware.objectobject.ca:3000"
_websocket_url = "wss://productiveware.objectobject.ca:3500"
_login_url = f"{base_url}/api/auth/login"

def request_token(username, password):
	response = requests.post(_login_url, json={"username": username, "password": password})
	if response.status_code == 401:
		raise PermissionError
	elif response.status_code != 200:
		raise RuntimeError(response.status_code)
	cookie = parse.unquote(response.cookies.get("connect.sid"))
	return re.search(":([^\.]+)", cookie).group(1)

def connect(token):
	pass

def get_encryption_key():
	"""Get the user's encryption key from the server."""
	return b"WkgJfErD7J_LqwX_hmAiFZfmVLOt1p7ZXpaCl0vdZgY=" # placeholder
