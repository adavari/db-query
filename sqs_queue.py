import json

import boto3

from credentials.credential_reader import Credentials
from dynamodb_formatter import dict_to_dynamodb


def send_to_output(credentials: Credentials, queue_name: str, rows: list):
    sqs = boto3.resource('sqs', aws_access_key_id=credentials.access_key_id,
                         aws_secret_access_key=credentials.secret_key)
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    for row in rows:
        queue.send_message(MessageBody=json.dumps(dict_to_dynamodb(row)))
