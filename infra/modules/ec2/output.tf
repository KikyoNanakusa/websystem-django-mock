output "ec2_instance_ids" {
  description = "List of EC2 instance IDs"
  value       = aws_instance.django[*].id
}

output "ec2_public_ips" {
  description = "List of EC2 public IPs"
  value       = aws_instance.django[*].public_ip
}

output "ec2_private_ips" {
  description = "List of EC2 private IPs"
  value       = aws_instance.django[*].private_ip
}