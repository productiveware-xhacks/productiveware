from . import encryption

_websocket_url = "wss://productiveware.objectobject.ca:3500"

class Client:
	def connect(self, token):

	def get_encryption_key(self):
		"""Get the user's encryption key from the server.
		
		If none exists, generate a new one and send it to the server, then return it."""
		return b"WkgJfErD7J_LqwX_hmAiFZfmVLOt1p7ZXpaCl0vdZgY=" # placeholder
