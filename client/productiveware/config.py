import json
from pathlib import Path
import os


_config_dir = os.getenv("APPDATA")+"\productiveware"
_config_file = _config_dir+"\config.json"


def _read():
	try:
		with open(_config_file, "r") as f:
			return json.load(f)
	except OSError:
		return {}

# might raise an exception if it fails to write to the file
def _write(config):
	Path(_config_dir).mkdir(exist_ok=True)
	with open(_config_file, "w") as f:
		json.dump(config, f)


def get_target_folders():
	config = _read()
	return config.get("target_folders", [])

def add_target_folder(path):
	config = _read()
	try:
		target_folders = config["target_folders"]
	except KeyError:
		config["target_folders"] = []
		target_folders = config["target_folders"]
	target_folders.append(path)
	_write(config)

def remove_target_folder(path):
	config = _read()
	target_folders = config.get("target_folders", [])
	try:
		target_folders.remove(path)
	except ValueError:
		pass
	else:
		_write(config)
