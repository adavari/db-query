import boto3
from boto3.dynamodb.conditions import Key
from credentials.credential_reader import Credentials
from query.query import Query


class QueryByMsisdn(Query):

    def __init__(self, credentials: Credentials, sk: str, msisdn: str, timestamp: list, equation: str):
        super(QueryByMsisdn, self).__init__(credentials)
        self.sk = sk
        self.timestamp = timestamp
        self.equation = equation
        self.msisdn = msisdn
        self.dynamo_db = boto3.resource('dynamodb', aws_access_key_id=credentials.access_key_id,
                                        aws_secret_access_key=credentials.secret_key)
        self.table = self.dynamo_db.Table('messages')

    def query(self) -> list:
        if self.equation == '>':
            t_k = Key('timestamp').gt(int(self.timestamp[0]))
        elif self.equation == '>=':
            t_k = Key('timestamp').gte(int(self.timestamp[0]))
        elif self.equation == '<':
            t_k = Key('timestamp').lt(int(self.timestamp[0]))
        elif self.equation == '<=':
            t_k = Key('timestamp').lte(int(self.timestamp[0]))
        elif self.equation == '=' or self.equation == '==':
            t_k = Key('timestamp').eq(int(self.timestamp[0]))
        elif self.equation == 'btw':
            t_k = Key('timestamp').between(int(self.timestamp[0]), int(self.timestamp[1]))
        else:
            raise ValueError('incorrect formula')

        response = self.table.query(
            IndexName='message_per_msisdn',
            KeyConditionExpression=Key('msisdn').eq(self.sk + "#msisdn#" + self.msisdn).__and__(t_k)
        )
        return self.normalize(response['Items'])

