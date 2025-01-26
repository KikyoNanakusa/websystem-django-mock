resource "aws_lb" "main" {
	name = "web-system-alb"
	internal = false # Allow public access
	load_balancer_type = "application"
	security_groups = var.security_group_ids
	subnets = var.subnet_ids
	enable_deletion_protection = false
	
	ip_address_type = "ipv4"

	tags = {
		Name = "web-system-alb"
	}
}

resource "aws_lb_target_group" "main" {
	name = "web-system-tg"
	target_type = "instance"
	port = 8000
	protocol = "HTTP"
	vpc_id = var.vpc_id

	health_check {
		healthy_threshold = 2
		unhealthy_threshold = 2
		interval = 30
		path = "/"
		protocol = "HTTP"
		timeout = 5
	}

	tags = {
		Name = "web-system-tg"
	}
}

resource "aws_lb_target_group_attachment" "main" {
	target_group_arn 	= aws_lb_target_group.main.arn
	target_id 			= var.target_ids[0]
}

resource "aws_lb_target_group_attachment" "main2" {
	target_group_arn 	= aws_lb_target_group.main.arn
	target_id 			= var.target_ids[1]
}

resource "aws_lb_listener" "main" {
	load_balancer_arn 	= aws_lb.main.arn
	port 				= "80"
	protocol 			= "HTTP"

	default_action {
		type = "fixed-response"

		fixed_response {
			content_type = "text/plain"
			message_body = "Not Found"
			status_code = "404"
		}
	}

	tags = {
		Name = "web-system-listener"
	}
}

resource "aws_lb_listener_rule" "main" {
	listener_arn = aws_lb_listener.main.arn
	action {
		type = "forward"
		target_group_arn = aws_lb_target_group.main.arn
	}
	
	condition {
		path_pattern {
			values = ["*"]
		}
	}
}