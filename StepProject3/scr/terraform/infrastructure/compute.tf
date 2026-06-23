data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "jenkins_master" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.jenkins_sg.id]
  key_name               = var.key_name
}

resource "aws_spot_instance_request" "jenkins_worker" {
  ami                    = data.aws_ami.ubuntu.id
  spot_price             = "0.015"
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.jenkins_sg.id]
  wait_for_fulfillment   = true
  key_name               = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              echo "${file("${path.module}/my-ssh-key.pub")}" >> /home/ubuntu/.ssh/authorized_keys
              EOF
}