output "instance_private_ip" {
  description = "Private Ip of the EC2 instance(s)"
  value       = aws_instance.ec2_instance.private_ip

}

output "instance_public_ip" {
  description = "Public Ip of the EC2 instance(s)"
  value       = aws_instance.ec2_instance.public_ip
}

# output "ubuntu_ami" {
#   value = data.aws_ami.ubuntu
# }
