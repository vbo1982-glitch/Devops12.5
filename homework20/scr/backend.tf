terraform {
  backend "s3" {
    bucket = "terraform-state-danit-devops-vitaliy-eu"
    key    = "vitaliy_bogoslavskiy/terraform.tfstate"
    region = "eu-central-1"
  }
}