import json

def hello(event, context):
    """Return a personalized greeting.

    GET /hello/{name}
    """

    # TODO Extract name from path parameter instead of query parameter
    # TODO Handle URL encoded characters
    name = event["queryStringParameters"]["name"]

    response = {
        "message": f"Hello, {name}!"
    }

    # TODO Return correct content type
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }

# TODO Implement handler for POST method calls
