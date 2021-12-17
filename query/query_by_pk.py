import boto3
from boto3.dynamodb.conditions import Key

from credentials.credential_reader import Credentials
from query.query import Query


class QueryByPk(Query):

    def __init__(self, credentials: Credentials, pk: str):
        super(QueryByPk, self).__init__(credentials)
        self.pk = pk
        self.dynamo_db = boto3.resource('dynamodb', aws_access_key_id=credentials.access_key_id,
                                        aws_secret_access_key=credentials.secret_key)
        self.table = self.dynamo_db.Table('messages')

    def query(self) -> list:
        response = self.table.query(
            KeyConditionExpression=Key('PK').eq(self.pk)
        )
        return self.normalize(response['Items'])
