Exercise 5 - Orchestration
==========================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

This exercise uses the [Serverless Step Functions](https://serverless.com/plugins/serverless-step-functions/) plugin. The state machine used in the exercises is defined in `process_temperatures.yml`.

### Gotchas

Step Functions can configured with various triggers, such as HTTP endpoints via API Gateway. This does not currently work in LocalStack unfortunately.

Instead use `sls invoke stepf ...` to test the state machine directly (see below for examples).

## Exercises

Deploy the Step Functions state machine to LocalStack: `sls deploy`

1. Post an event to Step Functions and check the LocalStack log to verify that it works:

   `sls invoke stepf -n ProcessTemperatures -d '{"temperature": 20}'`

2. Observe what happens when posting an event with an invalid temperature value:

   `sls invoke stepf -n ProcessTemperatures -d '{"temperature": -50}'`

3. Add error handling to the Step Functions state machine, catching validation errors and moving to a fallback Fail state (see TODOs in `process_temperatures.yml`).
