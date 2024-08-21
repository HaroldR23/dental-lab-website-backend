resource "aws_api_gateway_rest_api" "dlw_api_gateway" {
  name        = "dlw-api"
  description = "API for DLW FastAPI application"
}

resource "aws_api_gateway_resource" "dlw_api_resource" {
  rest_api_id = aws_api_gateway_rest_api.dlw_api_gateway.id
  parent_id   = aws_api_gateway_rest_api.dlw_api_gateway.root_resource_id
  path_part   = "{proxy+}"
}

resource "aws_api_gateway_method" "dlw_api_method" {
  rest_api_id   = aws_api_gateway_rest_api.dlw_api_gateway.id
  resource_id   = aws_api_gateway_resource.dlw_api_resource.id
  http_method   = "ANY"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "dlw_api_integration" {
  rest_api_id = aws_api_gateway_rest_api.dlw_api_gateway.id
  resource_id = aws_api_gateway_resource.dlw_api_resource.id
  http_method = aws_api_gateway_method.dlw_api_method.http_method
  type        = "AWS_PROXY"

  integration_http_method = "POST"
  uri                     = var.lambda_uri
}

resource "aws_api_gateway_deployment" "dlw_api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.dlw_api_gateway.id
  stage_name  = var.stage_name
}

resource "aws_lambda_permission" "dlw_api_gateway_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = var.lambda_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.dlw_api_gateway.execution_arn}/*/*"
}
