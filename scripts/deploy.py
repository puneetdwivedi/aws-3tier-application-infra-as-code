from utils.constants import (
    AWS_ACCESS_KEY,
    AWS_DEFAULT_REGION,
    AWS_SECRET_KEY,
    PDW_STACK_SANDBOX_CORE_INFRA,
    PDW_STACK_SANDBOX_CORE_INFRA_FILE_URL,
    PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS
)
from utils.services.cft import CloudFormationClient, CloudFormationStack


def deploy():
    """Creating the CloudFormation client with aws credentials"""
    cf_client = CloudFormationClient(
        AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_DEFAULT_REGION
    ).get_cf_client()

    """ Deploying Cloud Formation stack """
    template_parameters = [
        {"ParameterKey": "ProjectPartialsS3BucketName", "ParameterValue": PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS},
    ]

    cf_stack = CloudFormationStack(
        stack_name=PDW_STACK_SANDBOX_CORE_INFRA,
        template_url=PDW_STACK_SANDBOX_CORE_INFRA_FILE_URL,
        parameters=template_parameters,
        cf_client=cf_client,
    )

    cf_stack.deploy()


if __name__ == "__main__":
    deploy()
