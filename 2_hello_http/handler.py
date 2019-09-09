import json

def hello(event, context):
    """Return a personalized greeting.

    GET /hello?name={name}
    """

    # TODO Implement extracting the 'name' query parameter
    # See https://serverless.com/framework/docs/providers/aws/events/apigateway/#request-parameters
    name = "JavaZone"

    # TODO Extract name from path parameter instead of query parameter
    # TODO Handle URL encoded characters

    response = {
        "message": f"Hello, {name}!"
    }

    # TODO Return correct content type
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }

# TODO Implement handler for POST method calls
