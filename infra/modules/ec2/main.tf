resource "aws_instance" "django" {
	count = length(var.subnet_ids)
	ami = var.ami_id
	instance_type = var.instance_type
	key_name = "websystem-key-pair"
	subnet_id = element(var.subnet_ids, count.index)
	vpc_security_group_ids = var.security_group_ids
	tags = {
		Name = "web-system-django-${count.index}"
	}
	user_data = <<-EOF
            	#!/bin/bash
            	echo "DB_HOST=${var.db_endpoint}" >> /etc/environment
            	echo "DB_NAME=${var.db_name}" >> /etc/environment
            	echo "DB_USER=${var.db_user}" >> /etc/environment
            	echo "DB_PASSWORD=${var.db_password}" >> /etc/environment
				echo "DB_PORT=${var.db_port}" >> /etc/environment
				echo "DJANGO_SECRET_KEY=${var.django_secret_key}" >> /etc/environment
            	source /etc/environment
            	EOF
}