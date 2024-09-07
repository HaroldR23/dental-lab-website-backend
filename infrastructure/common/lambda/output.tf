output "dlw_function" {
  value = aws_lambda_function.dlw_fastapi_lambda
}

output "dlw_func_role" {
  value = aws_iam_role.dlw_lambda_exec_role
}
