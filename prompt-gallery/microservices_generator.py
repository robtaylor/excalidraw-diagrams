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

# Services layer
arch.service("auth", "Auth Service", x=100, y=480, color="blue")
arch.service("product", "Product Service", x=300, y=480, color="blue")
arch.service("order", "Order Service", x=500, y=480, color="blue")
arch.service("payment", "Payment Service", x=700, y=480, color="blue")

# Databases
arch.database("postgres", "PostgreSQL", x=300, y=640, color="green")
arch.database("redis", "Redis", x=500, y=640, color="green")

# Connections from User to Frontend
arch.connect("user", "frontend", "HTTPS")

# Frontend to Gateway
arch.connect("frontend", "gateway", "REST")

# Gateway to Services
arch.connect("gateway", "auth", "gRPC")
arch.connect("gateway", "product", "REST")
arch.connect("gateway", "order", "REST")
arch.connect("gateway", "payment", "gRPC")

# Services to Databases
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")
arch.connect("auth", "redis", "cache")
arch.connect("product", "redis", "cache")

arch.save("gallery_output/microservices.excalidraw")
print("Created: gallery_output/microservices.excalidraw")
