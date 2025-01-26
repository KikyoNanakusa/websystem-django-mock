output "vpc_id" {
	description = "VPC ID"
	value = aws_vpc.main.id
}

output "public_subnet1_id" {
	description = "Public Subnet 1 ID"
	value = aws_subnet.public1.id
}

output "public_subnet2_id" {
	description = "Public Subnet 2 ID"
	value = aws_subnet.public2.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = [aws_subnet.public1.id, aws_subnet.public2.id]
}