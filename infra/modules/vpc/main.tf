resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags = {
	Name = "web-system-vpc"
  }
}

resource "aws_subnet" "public1" {
	vpc_id = aws_vpc.main.id
	cidr_block = "10.0.0.0/24"
	map_public_ip_on_launch = true
	availability_zone = var.azs[0]
	tags = {
		Name = "web-system-subnet-public1"
	}
}

resource "aws_subnet" "public2" {
	vpc_id = aws_vpc.main.id
	cidr_block = "10.0.1.0/24"
	map_public_ip_on_launch = true
	availability_zone = var.azs[1]
	tags = {
		Name = "web-system-subnet-public2"
	}
}

resource "aws_internet_gateway" "main" {
	vpc_id = aws_vpc.main.id
	tags = {
		Name = "web-system-igw"
	}
}

resource "aws_route_table" "public" {
	vpc_id = aws_vpc.main.id
	tags = {
		Name = "web-system-rtb-public"
	}
}

resource "aws_route" "internet_access" {
	route_table_id = aws_route_table.public.id
	destination_cidr_block = "0.0.0.0/0"
	gateway_id = aws_internet_gateway.main.id
}

resource "aws_route_table_association" "public1" {
	subnet_id = aws_subnet.public1.id
	route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public2" {
	subnet_id = aws_subnet.public2.id
	route_table_id = aws_route_table.public.id
}