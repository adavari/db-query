import configparser


class Credentials:

    def __init__(self, access_key_id: str, secret_key: str):
        self.access_key_id = access_key_id
        self.secret_key = secret_key


class ConfigReader:

    def __init__(self, config_path: str):
        self.config_path = config_path
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)

    def get_profiles(self) -> list:
        return self.parser.sections()

    def get_credentials(self, profile: str) -> Credentials:
        key_id = self.parser[profile]['aws_access_key_id']
        secret_key = self.parser[profile]['aws_secret_access_key']
        return Credentials(key_id, secret_key)
