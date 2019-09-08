Exercise 1 - Hello!
===================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

## Exercises

Deploy the `hello` Lambda function to LocalStack: `sls deploy`

1. Call the function to verify it is running: `sls invoke -f hello`
2. Modify the function in `handler.py` to say something else, e.g. "Hello, JavaZone!"
3. Redeploy and test the updated function: `sls deploy function -f hello`
