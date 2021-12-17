from credentials.credential_reader import Credentials


class Query:

    def __init__(self, credentials: Credentials):
        self.credentials = credentials

    def query(self) -> list:
        pass

    @staticmethod
    def normalize(response: list) -> list:
        for item in response:
            item['timestamp'] = int(item['timestamp'])
            item['part'] = int(item['part'])
        return response
