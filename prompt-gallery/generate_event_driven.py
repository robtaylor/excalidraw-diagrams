#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create an event-driven architecture diagram
arch = ArchitectureDiagram()

# Title
arch.text_box(300, 30, "Event-Driven Architecture", font_size=24)

# Order Service (publisher)
arch.service("order_svc", "Order Service", x=350, y=120, color="blue")

# Event Bus
arch.component("event_bus", "Event Bus\n(Kafka/SNS)", x=320, y=280, width=180, height=80, color="orange")

# Event label
arch.text_box(280, 220, "OrderCreated event", font_size=14, color="gray")

# Consumer services
arch.service("inventory", "Inventory Service\n(reserves stock)", x=100, y=450, color="violet")
arch.service("notification", "Notification Service\n(sends email)", x=300, y=450, color="violet")
arch.service("analytics", "Analytics Service\n(tracks metrics)", x=500, y=450, color="violet")
arch.service("shipping", "Shipping Service\n(prepares label)", x=700, y=450, color="violet")

# Connections
arch.connect("order_svc", "event_bus", "publish")
arch.connect("event_bus", "inventory", "subscribe")
arch.connect("event_bus", "notification", "subscribe")
arch.connect("event_bus", "analytics", "subscribe")
arch.connect("event_bus", "shipping", "subscribe")

arch.save("gallery_output/event_driven.excalidraw")
print("Created: event_driven.excalidraw")
