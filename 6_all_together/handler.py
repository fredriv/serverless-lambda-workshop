import boto3
import json

from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url='http://localhost:4569')
temperatures_table = dynamodb.Table('temperatures')


def receive_event(event, context):
    temperature = json.loads(event['body'])['temperature']

    item = {
        'location': 'Oslo',
        'temperature': Decimal(temperature)
    }

    temperatures_table.put_item(Item=item)

    return {
        'statusCode': 200
    }


def run_pipeline(event, context):
    pass


def filter_temperature(event, context):
    pass


def enrich_location(event, context):
    pass


def write_temperature(event, context):
    pass


def get_temperatures(event, context):
    items = temperatures_table.scan()['Items']
    for item in items:
        item['temperature'] = float(item['temperature'])

    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {'Content-Type': 'application/json'}
    }
