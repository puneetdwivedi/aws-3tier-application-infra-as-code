import os
from pathlib import Path


from utils.constants import (
    AWS_ACCESS_KEY,
    AWS_DEFAULT_REGION,
    AWS_SECRET_KEY,
    PDW_STACK_SANDBOX_CORE_INFRA_FILE,
    PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS,
)
from utils.services.s3_manager import S3Manager


def pre_deploy():
    s3_mgr = S3Manager(
        access_key=AWS_ACCESS_KEY, secret_key=AWS_SECRET_KEY, region=AWS_DEFAULT_REGION
    )

    # creating the bucket
    s3_mgr.create_bucket(PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS)

    base_dir = os.getcwd()
    # upload cloud formation template
    cft_stack_template_file_path = os.path.join(base_dir, "stacks", PDW_STACK_SANDBOX_CORE_INFRA_FILE)
    s3_mgr.upload_file(
        cft_stack_template_file_path, PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS, PDW_STACK_SANDBOX_CORE_INFRA_FILE
    )


    # deploy each cft stack template file 
    root_dir = Path(base_dir)
    template_dir = root_dir / "templates"
    print(template_dir)
    for file in template_dir.iterdir():
        if file.is_file():
            s3_mgr.upload_file(
                file, PDW_S3_BUCKET_SANDBOX_PROJECT_PARTIALS, file.name
            )



if __name__ == "__main__":
    pre_deploy()