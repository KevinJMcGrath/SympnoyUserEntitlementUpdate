import jsonpickle

from pathlib import Path

config_path = Path("./config.json")

with open(config_path, 'r') as _config_file:
    _config = jsonpickle.decode(_config_file.read())

_cert_folder = f'./{_config["cert_folder"]}'
_cert = Path(f'{_cert_folder}/{_config["cert_filename"]}')
_key = Path(f'{_cert_folder/_config["key_filename"]}')

bot_certificate = (_cert, _key)
bot_username = _config['bot_username']
auth_base_url = f'{_config["auth_host"]}:{_config["auth_port"]}'
api_base_url = f'{_config["api_host"]}:{_config["api_port"]}'
obo_base_url = f'{_config["obo_host"]}:{_config["obo_port"]}'