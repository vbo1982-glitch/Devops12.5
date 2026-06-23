terraform {
  backend "s3" {
    bucket = "my-step-project-3-tf-state-bucket-123"
    key    = "infrastructure/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}