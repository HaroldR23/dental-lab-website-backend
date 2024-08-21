variable "image_ecr_uri" {
    description = "The URI of the ECR image to deploy"
    type        = string
}

variable "env_variables" {
    description = "The environment variables to set in the Lambda function"
    type        = map(string)
}
