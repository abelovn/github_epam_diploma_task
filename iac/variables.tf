variable "region" {
  default	= "us-east-2"
}

variable "dbpass" {
  default = "password1"  
}

variable "dbuser" {
  default = "root1"
}

variable "pub_subnet" {
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}