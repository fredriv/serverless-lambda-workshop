# Serverless Lambda workshop

Workshop on creating applications using Serverless Framework and AWS Lambda

## Setup

### Create and configure an AWS account

- Create a free AWS account: https://portal.aws.amazon.com/billing/signup#/start
- Create a new user for the workshop: https://console.aws.amazon.com/iam/home#/users$new
  - Enable both **Programmatic access** and **AWS Management Console access**
  - On next page, choose **Attach existing policies directly**
    - Select e.g. `AdministratorAccess` or `AWSLambdaFullAccess`
  - Navigate through next pages and **Create user**
  - On the result page, copy the **Access key ID** and **Secret access key**, or download the credentials CSV-file
- Install the AWS command line tools: https://aws.amazon.com/cli/

Put the access and secret keys from above in the AWS credentials file, `~/.aws/credentials`:
```
[default]
aws_access_key_id     = <your-access-key>
aws_secret_access_key = <your-secret-key>
```
or configure them in a different AWS profile if you already have a `[default]` profile, e.g. `[workshop]`. For more details, see https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

### Install Serverless Framework

- Install npm: https://www.npmjs.com/get-npm
- Install Serverless command line tools: `npm install -g serverless`
