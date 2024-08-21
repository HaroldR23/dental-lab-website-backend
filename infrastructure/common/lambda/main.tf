resource "aws_lambda_function" "dlw_fastapi_lambda" {
  function_name = "dlw-fastapi-function"
  role          = aws_iam_role.dlw_lambda_exec_role.arn
  package_type  = "Image"
  image_uri     = var.image_ecr_uri
  timeout       = 30
  memory_size   = 512

  environment {
    variables = var.env_variables
  }
}

resource "aws_iam_role" "dlw_lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  ]
}
