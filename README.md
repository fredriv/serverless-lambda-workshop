# Serverless Lambda workshop

Workshop on creating applications using Serverless Framework and AWS Lambda

## Initial setup

- Create a free AWS account: https://portal.aws.amazon.com/billing/signup#/start
- Create a new user for the workshop: https://console.aws.amazon.com/iam/home#/users$new
  - Enable both 'Programmatic access' and 'AWS Management Console access'
  - On next page, choose 'Attach existing policies directly'
    - Select either `AdministratorAccess` or `AWSLambdaFullAccess`
  - Navigate through next pages and 'Create user'
  - On result page, make not of the 'Access key ID' and 'Secret access key', or download the credentials CSV-file
- Install the AWS command line tools: https://aws.amazon.com/cli/
- Set up AWS credentials for the CLI, using the 'Access key ID' and 'Secret access key' from above: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
