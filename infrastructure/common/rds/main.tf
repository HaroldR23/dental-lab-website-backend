resource "aws_security_group" "rds_security_group" {
  name        = var.rds_security_group_name
  description = "Allow inbound traffic for RDS"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_db_instance" "dlw_postgres_instance" {
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "16.4"
  instance_class       = "db.t3.micro"
  db_name              = var.db_name
  username             = var.db_user
  password             = var.db_password
  parameter_group_name = "default.postgres16"
  skip_final_snapshot  = true
  publicly_accessible  = true
  vpc_security_group_ids = [aws_security_group.rds_security_group.id]

  tags = {
    Name = var.rds_tag_name
  }
}
