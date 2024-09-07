variable "image_ecr_uri" {
    description = "The URI of the ECR image to deploy"
    type        = string
}

variable "env_variables" {
    description = "The environment variables to set in the Lambda function"
    type        = map(string)
}

variable "function_name" {
    description = "The name of the Lambda function"
    type        = string
}

variable "lambda_exec_role" {
    description = "The name of the IAM role for the Lambda function"
    type        = string
}
