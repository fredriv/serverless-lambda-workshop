Serverless Lambda workshop
==========================

Workshop on creating applications using Serverless Framework and AWS Lambda.

Slides can be found here: https://www.slideshare.net/fredriv/building-applications-with-serverless-framework-and-aws-lambda-javazone-2019

## Setup

- Install npm: https://www.npmjs.com/get-npm
- Install Serverless command line tools: `npm install -g serverless`
- Install [Docker](https://docs.docker.com/install/#supported-platforms) and [Docker Compose](https://docs.docker.com/compose/install/)
- Pre-fetch Lambda Docker images:
  - `docker image pull localstack/localstack:0.10.2`
  - `docker image pull lambci/lambda:python3.7`
- Install Python 3 and pip:
  - Mac: https://wsvincent.com/install-python3-mac/
- Install [LocalStack AWS CLI wrapper](https://github.com/localstack/awscli-local): `pip install awscli-local`

## Running on local machine

To run the exercises on your local machine, we will use [LocalStack](https://github.com/localstack/localstack) to emulate AWS services.

- Start LocalStack with `docker-compose up` from the top-level directory
- On Mac, you may need to run `TMPDIR=/private$TMPDIR docker-compose up`

### Debugging

- To enable debug output in LocalStack, run with `DEBUG=1 docker-compose up`
- Debugging Serverless Framework commands: `SLS_DEBUG=* sls deploy --verbose`

### LocalStack Gotchas

Full redeploy and undeploy does not work properly in LocalStack. You need to
either redeploy individual functions (`sls deploy function -f <function-name>`)
or restart LocalStack and do a fresh `sls deploy`.

### AWS CLI wrapper (awslocal) on Windows

If you install awslocal (`pip install awscli-local`), it does not install a Windows script. See: https://github.com/localstack/awscli-local/issues/6 for a script you can use. Save this as a Batch file in the Python environments Scripts directory.

### Host configuration on Docker Machine

On Docker Machine, the endpoint will not be served on localhost. This requires two changes. Set the environment variable `LOCALSTACK_HOST` to the hostname or IP, e.g.: `export LOCALSTACK_HOST=192.168.99.100` or `set LOCALSTACK_HOST=192.168.99.100`. Second you must update the `serverless.yml` files in each project under `custom.localstack` add a `host` key, and set its value to `http://{hostname_or_ip}`

This is used by awslocal, and when outputting endpoint information in the Localstack client.

## Running on AWS (optional)

- Create a free AWS account: https://portal.aws.amazon.com/billing/signup#/start
- Create a new user for the workshop: https://console.aws.amazon.com/iam/home#/users$new
  - Enable both **Programmatic access** and **AWS Management Console access**
  - On next page, choose **Attach existing policies directly**
    - Select e.g. `AdministratorAccess` or `AWSLambdaFullAccess`
  - Navigate through next pages and **Create user**
  - On the result page, copy the **Access key ID** and **Secret access key**, or download the credentials CSV-file
- Install the AWS command line tools: https://aws.amazon.com/cli/
- In each exercise directory:
  - Comment out the `serverless-localstack` plugin in the `serverless.yml` files

Put the access and secret keys from above in the AWS credentials file, `~/.aws/credentials`:
```
[default]
aws_access_key_id     = <your-access-key>
aws_secret_access_key = <your-secret-key>
```
or configure them in a different AWS profile if you already have a `[default]` profile, e.g. `[workshop]`. For more details, see https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

