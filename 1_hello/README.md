Exercise 1 - Hello!
===================

## Setup

- Install Serverless plugins: `npm install`
- Start LocalStack, see top level [README](../README.md)

## Exercises

1. Deploy the `hello` Lambda function to LocalStack: `sls deploy`
2. Call the function to verify it is running: `sls invoke -f hello`
3. Modify the function in `handler.py` to say e.g. "Hello, JavaZone!"
4. Redeploy and test the updated function: `sls deploy function -f hello`
