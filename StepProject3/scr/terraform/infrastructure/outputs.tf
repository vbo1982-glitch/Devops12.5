output "jenkins_master_public_ip" {
  value = aws_instance.jenkins_master.public_ip
}

output "jenkins_worker_private_ip" {
  value = aws_spot_instance_request.jenkins_worker.private_ip
}