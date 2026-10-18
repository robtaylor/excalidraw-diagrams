#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create an architecture diagram for an e-commerce platform
arch = ArchitectureDiagram()

# User
arch.user("user", "User", x=400, y=50)

# Frontend
arch.component("frontend", "Web Frontend", x=350, y=180, color="blue")

# API Gateway
arch.service("gateway", "API Gateway", x=350, y=320, color="violet")

# Services row
arch.service("auth", "Auth Service", x=100, y=480, color="blue")
arch.service("product", "Product Service", x=300, y=480, color="blue")
arch.service("order", "Order Service", x=500, y=480, color="blue")
arch.service("payment", "Payment Service", x=700, y=480, color="blue")

# Databases row
arch.database("postgres", "PostgreSQL", x=300, y=640, color="green")
arch.database("redis", "Redis", x=500, y=640, color="red")

# Connections from User to Frontend
arch.connect("user", "frontend", "HTTPS")

# Frontend to Gateway
arch.connect("frontend", "gateway", "REST")

# Gateway to Services
arch.connect("gateway", "auth", "REST")
arch.connect("gateway", "product", "REST")
arch.connect("gateway", "order", "gRPC")
arch.connect("gateway", "payment", "gRPC")

# Services to Databases
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")
arch.connect("product", "redis", "Cache")
arch.connect("order", "redis", "Cache")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/microservices.excalidraw"
arch.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(arch.elements)}")
