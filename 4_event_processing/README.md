Exercise 4 - Event processing
=============================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

The SQS queue and Kinesis stream used in the exercises are already configured in the `Resources` section of `serverless.yml`.

## Exercises

1. Set up event handler for SQS queue `my-queue` on the `handle_sqs` function in `serverless.yml`

2. Post a message to SQS queue and check the LocalStack log to verify that it works:

   `awslocal sqs list-queues`

   `awslocal sqs send-message --message-body "Hello, JavaZone" --queue-url <queue-url>`

3. Set up an event handler for the SNS topic `my-topic` in `serverless.yml`
   and implement the function in `handler.py`

   - Hint: For SNS event handler you can just specify the topic name and Serverless Framework creates the SNS topic for you

4. Publish a message to the SNS topic and check the LocalStack log to verify that it works:

   `awslocal sns list-topics`

   `awslocal sns publish --message "Hello, JavaZone" --topic-arn <topic-arn>`

5. Set up an event handler for the Kinesis stream `my-stream` in `serverless.yml`
   and implement the function in `handler.py`

   - Hint: The AWS region and account number to use for the stream ARN in the event handler are `eu-west-1` and `000000000000`.

4. Post a message to the Kinesis stream and check LocalStack log to verify that it works:

   `awslocal kinesis list-streams`

   `awslocal kinesis put-record --data "Hello, JavaZone" --partition-key foo --stream-name my-stream`
