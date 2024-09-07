resource "aws_ecr_repository" "dlw_api_ecr" {
  name                 = var.ecr_name
}

resource "aws_ecr_lifecycle_policy" "dlw_ecr_retain_5_images" {
  repository = aws_ecr_repository.dlw_api_ecr.name

  policy = <<POLICY
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep last 5 images",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 5
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
POLICY
}
