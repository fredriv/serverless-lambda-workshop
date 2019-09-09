Exercise 2 - Hello HTTP!
========================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

## Exercises

Deploy the `hello` Lambda function to LocalStack: `sls deploy`

1. Test the API using e.g. [HTTPie](https://httpie.org/), curl or your browser
   - You can find the URL in the output of the deploy command, or run `sls info`
2. Make the function return the correct content type `application/json`
3. Change the function to receive a name as a query parameter
4. Change the function handler and configuration in `serverless.yml` to use path parameter instead of query parameter
   - i.e. `http://<base-url>/hello/<name>`
5. Add handler for POST method, receiving `name` parameter in JSON object in message body
6. Handle URL encoding of query parameters, e.g. `%20` as space
   - Hint: Check out `urllib.parse` in Python library
7. Handle `+` character as space in query parameters, e.g. `JavaZone+2019`
