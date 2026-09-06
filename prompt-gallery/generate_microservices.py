#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# E-commerce platform with multiple services
arch = ArchitectureDiagram()

# Client layer
arch.user("user", "User", x=400, y=50)

# Frontend
arch.component("frontend", "Web Frontend", x=350, y=170, color="blue")

# API Gateway
arch.service("gateway", "API Gateway", x=350, y=310, color="violet")

# Services layer
arch.service("auth", "Auth Service", x=100, y=470, color="blue")
arch.service("product", "Product Service", x=300, y=470, color="blue")
arch.service("order", "Order Service", x=500, y=470, color="blue")
arch.service("payment", "Payment Service", x=700, y=470, color="blue")

# Database layer
arch.database("postgres", "PostgreSQL", x=250, y=630, color="green")
arch.database("redis", "Redis", x=550, y=630, color="red")

# Connections from User to Frontend
arch.connect("user", "frontend", "HTTPS")

# Frontend to Gateway
arch.connect("frontend", "gateway", "REST")

# Gateway to Services
arch.connect("gateway", "auth", "REST")
arch.connect("gateway", "product", "gRPC")
arch.connect("gateway", "order", "REST")
arch.connect("gateway", "payment", "gRPC")

# Services to Databases
arch.connect("auth", "postgres", "SQL")
arch.connect("product", "postgres", "SQL")
arch.connect("order", "postgres", "SQL")
arch.connect("payment", "postgres", "SQL")

# Services to Redis
arch.connect("auth", "redis", "Cache")
arch.connect("product", "redis", "Cache")

arch.save("gallery_output/microservices.excalidraw")
print("Created: gallery_output/microservices.excalidraw")
