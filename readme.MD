create a vpc named 
pdw-vpc-lab-dev 
cidr: 10.0.0.0/16

subnet:
1 public 10.0.1.0/24
2 private can access internet 10.0.2.0/24
3 private complete private no outside just 10.0.3.0/24

nat gateway for 2nd subnet
nacl on 3rd subnet to only access via http and not via ssh

pdw-<service>-<env>-<purpose>-<seq>

- create vpc
- create 6subnet - (1 public , 2private ) in two region
- create internet gateway -
- create 3 route table -for each subnet
- create route table subnet association
- create elastic ip for nat gateway
- create nat gateway 
- create s3 bucket - ui infra
- bucket policy to ui infra bucket
- cloudfront resorce and its origin as s3
- prepare frontend application


- prepare backend application
- make docker image 
- create rds aurora postgres db
- ecs(launch type ec2) - task definition, service, alb listner, alb target group, ec2 launch template , ec2 asg, 
ecs instance profile(required for ), ecs instance role


test until this point




