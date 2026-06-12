provider "aws" {
  region = "eu-central-1"
}

data "aws_vpc" "default" {
  default = true
}

module "nginx_server" {
  source             = "./modules/nginx-ec2"
  vpc_id             = data.aws_vpc.default.id
  list_of_open_ports = [80, 22]
}