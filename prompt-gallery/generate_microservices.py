#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create architecture diagram for e-commerce platform
arch = ArchitectureDiagram()

# User at top
user = arch.user("user", "User", x=400, y=50)

# Web Frontend
frontend = arch.component("frontend", "Web Frontend", x=350, y=180, color="blue")

# API Gateway
gateway = arch.service("gateway", "API Gateway", x=350, y=320, color="violet")

# Services layer - arranged horizontally
auth_svc = arch.service("auth", "Auth Service", x=50, y=480, color="blue")
product_svc = arch.service("product", "Product Service", x=250, y=480, color="blue")
order_svc = arch.service("order", "Order Service", x=450, y=480, color="blue")
payment_svc = arch.service("payment", "Payment Service", x=650, y=480, color="blue")

# Databases
postgres = arch.database("postgres", "PostgreSQL", x=250, y=640, color="green")
redis = arch.database("redis", "Redis", x=450, y=640, color="green")

# Connections
arch.connect("user", "frontend", "HTTPS")
arch.connect("frontend", "gateway", "REST")

# Gateway to services
arch.connect("gateway", "auth", "gRPC")
arch.connect("gateway", "product", "REST")
arch.connect("gateway", "order", "REST")
arch.connect("gateway", "payment", "gRPC")

# Services to databases
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")

# Redis connections
arch.connect("auth", "redis", "Cache")
arch.connect("product", "redis", "Cache")

arch.save("gallery_output/microservices.excalidraw")
print("Created: gallery_output/microservices.excalidraw")
