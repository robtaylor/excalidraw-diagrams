#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create an architecture diagram for an e-commerce platform
arch = ArchitectureDiagram()

# User layer
arch.user("user", "User", x=400, y=50)

# Frontend
arch.component("frontend", "Web Frontend", x=350, y=180, color="blue")

# API Gateway
arch.service("gateway", "API Gateway", x=350, y=320, color="violet")

# Services layer
arch.service("auth", "Auth Service", x=100, y=480, color="blue")
arch.service("product", "Product Service", x=280, y=480, color="blue")
arch.service("order", "Order Service", x=460, y=480, color="blue")
arch.service("payment", "Payment Service", x=640, y=480, color="blue")

# Database layer
arch.database("postgres", "PostgreSQL", x=200, y=640, color="green")
arch.database("redis", "Redis", x=520, y=640, color="orange")

# Connections
arch.connect("user", "frontend", "HTTPS")
arch.connect("frontend", "gateway", "REST")
arch.connect("gateway", "auth", "REST")
arch.connect("gateway", "product", "REST")
arch.connect("gateway", "order", "gRPC")
arch.connect("gateway", "payment", "gRPC")
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")
arch.connect("product", "redis", "Cache")
arch.connect("order", "redis", "Cache")

arch.save("gallery_output/microservices.excalidraw")
print("Created: microservices.excalidraw")
