variable "lambda_uri" {
    description = "URI of the Lambda function to integrate with the API Gateway"
    type = string
}

variable "stage_name" {
    description = "Name of the stage to deploy the API Gateway to"
    type = string
}

variable "lambda_name" {
    description = "Name of the Lambda function to integrate with the API Gateway"
    type = string
}

variable "api_name" {
    description = "Name of the API Gateway"
    type = string
}
