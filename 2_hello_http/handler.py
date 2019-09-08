import json
from urllib.parse import unquote_plus

def hello(event, context):
    """Return a personalized greeting.

    GET /hello?name={name}
    """

    # TODO Implement extracting the 'name' query parameter
    # See https://serverless.com/framework/docs/providers/aws/events/apigateway#example-lambda-proxy-event-default

    # TODO Extract name from path parameter instead of query parameter
    # See https://serverless.com/framework/docs/providers/aws/events/apigateway/#request-parameters

    # TODO Handle URL encoded characters
    name = unquote_plus(event["pathParameters"]["name"])

    response = {
        "message": f"Hello, {name}!"
    }

    # TODO Return correct content type
    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": {"Content-Type": "application/json"}
    }

# TODO Implement handler for POST method calls
def hello_post(event, context):
    name = json.loads(event["body"])["name"]

    response = {
        "message": f"Hello, {name}!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": {"Content-Type": "application/json"}
    }
