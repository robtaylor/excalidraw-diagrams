#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create architecture diagram for e-commerce platform
arch = ArchitectureDiagram()

# Title
arch.text_box(250, 30, "E-Commerce Microservices Architecture", font_size=24)

# User
arch.user("user", "User", x=350, y=100)

# Frontend
arch.component("frontend", "Web Frontend", x=300, y=220, color="blue")

# API Gateway
arch.service("gateway", "API Gateway", x=280, y=360, color="violet")

# Services layer
arch.service("auth", "Auth Service", x=80, y=520, color="blue")
arch.service("product", "Product Service", x=260, y=520, color="blue")
arch.service("order", "Order Service", x=440, y=520, color="blue")
arch.service("payment", "Payment Service", x=620, y=520, color="blue")

# Databases
arch.database("postgres", "PostgreSQL", x=200, y=680, color="green")
arch.database("redis", "Redis", x=480, y=680, color="orange")

# Connections with protocol labels
arch.connect("user", "frontend", "HTTPS")
arch.connect("frontend", "gateway", "REST API")
arch.connect("gateway", "auth", "gRPC")
arch.connect("gateway", "product", "REST")
arch.connect("gateway", "order", "REST")
arch.connect("gateway", "payment", "gRPC")
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")
arch.connect("auth", "redis", "Cache")
arch.connect("product", "redis", "Cache")

arch.save("gallery_output/microservices.excalidraw")
print("✓ Created: gallery_output/microservices.excalidraw")
