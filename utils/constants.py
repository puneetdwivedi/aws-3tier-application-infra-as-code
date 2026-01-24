import os
from dotenv import load_dotenv

# loading env variables
load_dotenv()


# env variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", 'ap-south-1')
RDS_DB_USERNAME = os.getenv("RDS_DB_USERNAME")



# constants
PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS = "pdw-s3-bucket-sandbox-project-partials"
PDW_STACK_SANDBOX_CORE_INFRA = "pdw-stack-sandbox-core-infra"
PDW_STACK_SANDBOX_CORE_INFRA_FILE = f"{PDW_STACK_SANDBOX_CORE_INFRA}.yml"
PDW_STACK_SANDBOX_CORE_INFRA_FILE_URL = f"https://{PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS}.s3.{AWS_DEFAULT_REGION}.amazonaws.com/{PDW_STACK_SANDBOX_CORE_INFRA_FILE}"