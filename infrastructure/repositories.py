import os
import boto3
from botocore.exceptions import ClientError
from infrastructure.abstracts_repositories import AbstractRepository
from domain.domain import Task
from domain.exceptions import BaseException, DadosInvalidosError


class TaskRepository(AbstractRepository):

    def __init__(self) -> None:
        self.table_name = 'TasksTable'
        self.dynamodb = boto3.resource('dynamodb',
                                       aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                                       aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
                                       endpoint_url=os.getenv('DYNAMODB_URL'),
                                       region_name="local")
        self.table = self.dynamodb.Table(self.table_name)

    def get_all_items(self):
        try:
            response = self.table.scan()
            return [Task.from_dict(task) for task in response['Items']]
        except ClientError as e:
            print(f'Error retrieving tasks: {e.response["Error"]["Message"]}')
            return []

    def get_item(self, task_id: str):
        try:
            response = self.table.get_item(Key={'id': task_id})
            task = Task.from_dict(response.get('Item'))
            return task
        except ClientError as e:
            print(f'Error retrieving task: {e.response["Error"]["Message"]}')
            raise BaseException()
        except DadosInvalidosError:
            raise DadosInvalidosError("ID não encontrado")

    def save_item(self, task: Task):
        try:
            self.table.put_item(Item=task.to_dict())
        except ClientError as e:
            print(f'Error saving task: {e.response["Error"]["Message"]}')
            raise BaseException()

    def update_item(self, task_id: str, update_data: dict):
        try:
            self.table.update_item(Key={'id': task_id},
                                   UpdateExpression=self._generate_update_expression(update_data),
                                   ExpressionAttributeValues=self._generate_expression_attribute_values(update_data),
                                   ExpressionAttributeNames=self._generate_expression_attribute_names(update_data))
        except ClientError as e:
            print(f'Error saving task: {e.response["Error"]["Message"]}')
            raise BaseException()

    def delete_item(self, task_id: str):
        try:
            self.table.delete_item(Key={'id': task_id})
        except ClientError as e:
            print(f'Error saving task: {e.response["Error"]["Message"]}')
            raise BaseException('Item não encontrado')
