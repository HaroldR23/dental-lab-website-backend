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
