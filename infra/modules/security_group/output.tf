output "django_security_group_id" {
  description = "ID of the security group for Django"
  value       = aws_security_group.django.id
}

output "rds_security_group_id" {
  description = "ID of the security group for RDS"
  value       = aws_security_group.rds.id
}
