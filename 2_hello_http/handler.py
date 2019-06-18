import json

def hello(event, context):
    """Return a personalized greeting.

    GET /hello/{name}
    """

    name = event["pathParameters"]["name"]

    response = {
        "message": f"Hello, {name}!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
