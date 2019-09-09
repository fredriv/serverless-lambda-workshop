Exercise 5 - Orchestration
==========================

## Setup

- Install Serverless plugins: `npm install` (first time)
- Start LocalStack, see top level [README](../README.md)

The Step Functions state machine used in the exercises is already configured in `serverless.yml` and `process_temperatures.yml`.

## Exercises

Deploy the Step Functions state machine to LocalStack: `sls deploy`

1. Post an event to Step Functions and check the LocalStack log to verify that it works:

   `sls invoke stepf -n ProcessTemperatures -d '{"temperature": 20}'`
