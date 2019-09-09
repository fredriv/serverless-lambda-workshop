import base64

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_sqs(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

    for record in event["Records"]:
        msg = record["body"]
        logger.info(f"Got SQS event: {msg}")

def handle_sns(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    # TODO Implement event handler for SNS topic

def handle_kinesis(event, content):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    # TODO Implement event handler for Kinesis stream
    # Hint: Use base64.b64decode to decode event data
