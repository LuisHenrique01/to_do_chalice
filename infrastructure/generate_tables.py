import os
import boto3


def create_table(table_name: str = 'TasksTable'):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                              aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
                              endpoint_url=os.getenv('DYNAMODB_URL'),
                              region_name="local")
    table_creation_resp = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print(table_creation_resp)
