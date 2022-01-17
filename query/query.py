from credentials.credential_reader import Credentials


class Query:

    def __init__(self, credentials: Credentials):
        self.credentials = credentials

    def query(self) -> list:
        pass

    @staticmethod
    def normalize(response: list) -> list:
        for item in response:
            if 'timestamp' in item:
                item['timestamp'] = int(item['timestamp'])
            if 'part' in item:
                item['part'] = int(item['part'])
            if 'msisdn' in item:
                del item['msisdn']
            if 'internalDataCoding' in item:
                item['internalDataCoding'] = int(item['internalDataCoding'])
        return response
