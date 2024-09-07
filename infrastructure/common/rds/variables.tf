variable "db_name" {
    description = "The name of the database"
    type        = string
    sensitive   = true  
}

variable "db_user" {
    description = "The username for the database"
    type        = string
    sensitive   = true
}

variable "db_password" {
    description = "The password for the database"
    type        = string
    sensitive   = true
}

variable "rds_tag_name" {
    description = "The tag name for the RDS instance"
    type        = string
}

variable "rds_security_group_name" {
    description = "The name of the security group for the RDS instance"
    type        = string
}
