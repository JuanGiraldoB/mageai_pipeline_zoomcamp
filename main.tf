terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    # The bucket has to be previously created
    bucket  = "your-s3-bucket"
    key     = "your-key"
    region  = "us-east-1"
    profile = "terraform"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Create a Bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "your-s3-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}