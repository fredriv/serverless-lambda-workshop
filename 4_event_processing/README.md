Exercise 4 - Event processing
=============================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

## Exercises

Deploy Serverless functions and resources: `sls deploy`

1. In `serverless.yml`, set up event mapping for SQS queue `my-queue`
   on the `handle_sqs` function
   - https://serverless.com/framework/docs/providers/aws/events/sqs/
   - The ARN for the event mapping is `arn:aws:sqs:us-east-1:000000000000:my-queue`

2. Post a message to SQS queue and check the log messages in LocalStack to verify that it works:

  ```
  awslocal sqs list-queues

  awslocal sqs send-message --queue-url <queue-url> --message-body "Hello, JavaZone"
  ```

3. Configure an event handler and mapping for the SNS topic `my-topic` in `serverless.yml`
   and implement the function in `handler.py`
   - https://serverless.com/framework/docs/providers/aws/events/sns/

4. Post a message to the SNS topic and check the log messages in LocalStack to verify that it works:

  ```
  awslocal sns list-topics

  awslocal sns publish --topic-arn <topic-arn> --message "Hello, JavaZone"
  ```

5. Configure an event handler and mapping for the Kinesis stream `my-stream` in `serverless.yml`
   and implement the function in `handler.py`
   - https://serverless.com/framework/docs/providers/aws/events/streams/

4. Post a message to the Kinesis stream and check the log messages in LocalStack to verify that it works:

  ```
  awslocal kinesis list-streams

  awslocal kinesis put-record --stream-name my-stream --partition-key 1 --data "Hello, JavaZone"
  ```

### Hints:

- The AWS region and account number to use for the event mappings
  are `us-east-1` and `000000000000`.
- The SQS queue and Kinesis streams are already configured in the
  `Resources` section of `serverless.yml`.
- The SNS topic is created by Serverless Framework by default.

