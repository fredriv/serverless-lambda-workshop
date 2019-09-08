Exercise 2 - Hello HTTP!
========================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

## Exercises

Deploy the `hello` Lambda function to LocalStack: `sls deploy`
Make note of URL endpoint of the REST API in the Serverless Framework output (or run `sls info`).

1. Return correct content type `application/json`
2. Change the handler function to use path parameters instead of query parameters
2. Handle URL encoding of query parameters, e.g. `%20` as space
   - Hint: Check out `urllib.parse` in Python library
3. Handle `+` character as space in query parameters, e.g. `JavaZone+2019`
4. Add handler for POST method, receiving `name` parameter in JSON object in message body
