def handle_event(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    for record in event["Records"]:
        msg = record["Sns"]["Message"]

        print(f"Got event: {msg}")
