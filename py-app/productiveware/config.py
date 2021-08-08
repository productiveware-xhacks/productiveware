import json
from pathlib import Path
import os


_config_dir = os.path.join(os.getenv("APPDATA"), "productiveware")
_config_file = os.path.join(_config_dir, "config.json")
_log_file = os.path.join(_config_dir, "encryption.log")


def _read_config():
	try:
		with open(_config_file, "r") as f:
			return json.load(f)
	except OSError:
		return {}

# might raise an exception if it fails to write to the file
def _write_config(config):
	Path(_config_dir).mkdir(exist_ok=True)
	with open(_config_file, "w") as f:
		json.dump(config, f)


def get_log():
	try:
		with open(_log_file, "r") as f:
			return f.read().rstrip()
	except OSError:
		return ""

def add_to_log(text):
	with open(_log_file, "a") as f:
		f.write(text.rstrip()+"\n")

def get_target_folders():
	config = _read_config()
	return config.get("target_folders", [])

def add_target_folder(path):
	config = _read_config()
	try:
		target_folders = config["target_folders"]
	except KeyError:
		config["target_folders"] = []
		target_folders = config["target_folders"]
	target_folders.append(path)
	_write_config(config)

def remove_target_folder(path):
	config = _read_config()
	target_folders = config.get("target_folders", [])
	try:
		target_folders.remove(path)
	except ValueError:
		pass
	else:
		_write_config(config)

def clear_target_folders():
	config = _read_config()
	config["target_folders"] = []
	_write_config(config)

def get_cookie():
	config = _read_config()
	return config.get("cookie", None)

def set_cookie(cookie):
	config = _read_config()
	config["cookie"] = cookie
	_write_config(config)