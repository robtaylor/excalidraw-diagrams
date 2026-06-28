#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create microservices architecture diagram
arch = ArchitectureDiagram()

# Title
arch.diagram.text_box(250, 30, "E-commerce Microservices Architecture", font_size=24)

# User at top
arch.user("user", "User", x=400, y=100)

# Web frontend
arch.component("frontend", "Web Frontend", x=350, y=230, color="blue")

# API Gateway
arch.service("gateway", "API Gateway", x=350, y=370, color="violet")

# Services row
arch.service("auth", "Auth Service", x=100, y=510, color="blue")
arch.service("product", "Product Service", x=300, y=510, color="blue")
arch.service("order", "Order Service", x=500, y=510, color="blue")
arch.service("payment", "Payment Service", x=700, y=510, color="blue")

# Databases row
arch.database("postgres", "PostgreSQL", x=300, y=680, color="green")
arch.database("redis", "Redis", x=500, y=680, color="red")

# Connections
arch.connect("user", "frontend", "HTTPS")
arch.connect("frontend", "gateway", "REST")
arch.connect("gateway", "auth", "REST")
arch.connect("gateway", "product", "gRPC")
arch.connect("gateway", "order", "gRPC")
arch.connect("gateway", "payment", "REST")
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")
arch.connect("product", "redis", "Cache")
arch.connect("order", "redis", "Session")

arch.save("gallery_output/microservices.excalidraw")
print("Created: gallery_output/microservices.excalidraw")
