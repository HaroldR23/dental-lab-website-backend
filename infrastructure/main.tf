provider "aws" {
  region = local.region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-bucket-dlw"
    key    = "terraform/state/dlw_state.tfstate" # There's no way, i have to create the s3 bucket first to store the state file
    region = "us-east-1"
  }
}

####### EXTERNAL DATA ########
data "external" "sops-secrets" {
  program = ["sops", "-d", local.secrets_file]
}

########   ECR   #########
module "ecr" {
  source   = "./common/ecr"
  ecr_name = local.ecr_name
}

#########  LAMBDA  #########
module "lambda" {
  source           = "./common/lambda"
  image_ecr_uri    = module.ecr.ecr_resource.repository_url
  function_name    = local.function_name
  lambda_exec_role = local.lambda_exec_role
  env_variables = {
    SQL_URL         = sensitive("postgresql://${data.external.sops-secrets.result["DB_USER"]}:${data.external.sops-secrets.result["DB_PASSWORD"]}@${module.rds.db_instance.address}:5432/${data.external.sops-secrets.result["DB_NAME"]}"),
    SENDER_EMAIL    = sensitive(data.external.sops-secrets.result["SENDER_EMAIL"]),
    SENDER_PASSWORD = sensitive(data.external.sops-secrets.result["SENDER_PASSWORD"]),
  }
}

#########  API GATEWAY  #########
module "api_gateway" {
  source      = "./common/api_gateway"
  lambda_name = module.lambda.dlw_function.function_name
  lambda_uri  = module.lambda.dlw_function.invoke_arn
  stage_name  = local.environment
  api_name    = local.api_name
}


#########  RDS  #########
module "rds" {
  source       = "./common/rds"
  db_name      = sensitive(data.external.sops-secrets.result["DB_NAME"])
  db_password  = sensitive(data.external.sops-secrets.result["DB_PASSWORD"])
  db_user      = sensitive(data.external.sops-secrets.result["DB_USER"])
  rds_tag_name = local.rds_tag_name
  rds_security_group_name = local.rds_security_group_name
}
