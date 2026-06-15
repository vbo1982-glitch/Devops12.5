provider "aws" {
region = "us-east-1"
}

data "aws_ami" "ubuntu" {
most_recent = true
filter {
name   = "name"
values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
}
owners = ["099720109477"]
}

resource "aws_security_group" "web_sg" {
name        = "web_sg_nginx"
description = "Allow SSH and HTTP"

ingress {
from_port   = 22
to_port     = 22
protocol    = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}

ingress {
from_port   = 80
to_port     = 80
protocol    = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}

egress {
from_port   = 0
to_port     = 0
protocol    = "-1"
cidr_blocks = ["0.0.0.0/0"]
}
}

resource "aws_instance" "web" {
count                  = 2
ami                    = data.aws_ami.ubuntu.id
instance_type          = "t3.micro"
vpc_security_group_ids = [aws_security_group.web_sg.id]
key_name               = "my-ssh-key"

tags = {
Name = "Nginx-Server-${count.index + 1}"
}
}

resource "local_file" "ansible_inventory" {
content = <<EOT
[webservers]
%{ for ip in aws_instance.web.*.public_ip ~}
${ip} ansible_user=ubuntu ansible_ssh_common_args='-o StrictHostKeyChecking=no'
%{ endfor ~}
EOT
filename = "inventory.ini"
}