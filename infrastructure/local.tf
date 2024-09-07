locals {
  environment      = terraform.workspace
  secrets_file     = "api-dlw-${local.environment}-secrets.json"
  ecr_name         = "dlw-${local.environment}-repository"
  function_name    = "dlw-${local.environment}-fastapi-function"
  lambda_exec_role = "dlw-${local.environment}-lambda-exec-role"
  api_name         = "dlw-${local.environment}-api"
  rds_tag_name     = "fastapi-${local.environment}-postgres"
  region           = "us-east-1"
  rds_security_group_name = "dlw-${local.environment}-rds-security-group"
}
