import base64

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_sqs(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

    for record in event["Records"]:
        msg = record["body"]
        logger.info(f"Got event: {msg}")

    return {"status": "ok"}

def handle_sns(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    # TODO Implement event handler for SNS topic
    for record in event["Records"]:
        # TODO Extract message from record and log it
        pass
        msg = record["Sns"]["Message"]
        logger.info(f"Got event: {msg}")

    return {"status": "ok"}

def handle_kinesis(event, content):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    # TODO Implement event handler for Kinesis stream
    
    for record in event["Records"]:
        # TODO Extract message from record and log it
        pass
        msg = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        logger.info(f"Got event: {msg}")

    return {"status": "ok"}
