import json
import os
import boto3

# LocalStack automatically injects LOCALSTACK_HOSTNAME inside Lambda containers.
# If running inside LocalStack Lambda, connect via LOCALSTACK_HOSTNAME, otherwise fallback to AWS_ENDPOINT_URL.
localstack_host = os.environ.get("LOCALSTACK_HOSTNAME")
endpoint_url = f"http://{localstack_host}:4566" if localstack_host else os.environ.get("AWS_ENDPOINT_URL")

dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
table_name = os.environ.get("TABLE_NAME", "UsersTable")

def handler(event, context):
    table = dynamodb.Table(table_name)
    
    table.put_item(
        Item={
            'userId': 'usr-1001',
            'name': 'DevOps Candidate',
            'status': 'Active'
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'User inserted successfully into LocalStack DynamoDB!'})
    }