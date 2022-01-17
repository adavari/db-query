import boto3
from boto3.dynamodb.conditions import Key
from credentials.credential_reader import Credentials
from query.query import Query


class QueryBySkTimestamp(Query):

    def __init__(self, credentials: Credentials, sk: str, timestamp: list, equation: str):
        super(QueryBySkTimestamp, self).__init__(credentials)
        self.sk = sk
        self.timestamp = timestamp
        self.equation = equation
        self.dynamo_db = boto3.resource('dynamodb', aws_access_key_id=credentials.access_key_id,
                                        aws_secret_access_key=credentials.secret_key, aws_session_token=credentials.token)
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
            IndexName='message_per_customer',
            KeyConditionExpression=Key('SK').eq(self.sk).__and__(t_k)
        )

        data = response.get('Items')
        while 'LastEvaluatedKey' in response:
            response = self.table.query(
                IndexName='message_per_customer',
                KeyConditionExpression=Key('SK').eq(self.sk).__and__(t_k),
                LastEvaluatedKey=response['LastEvaluatedKey']
            )
            data.extend(response['Items'])

        return self.normalize(data)

