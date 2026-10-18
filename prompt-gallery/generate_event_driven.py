#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create an event-driven architecture diagram
arch = ArchitectureDiagram()

# Title
arch.text_box(300, 30, "Event-Driven Architecture", font_size=24, color="black")

# Order Service (publisher)
arch.service("order_service", "Order Service", x=100, y=150, color="blue")

# Event Bus (center)
arch.component("event_bus", "Event Bus\n(Kafka/SNS)", x=400, y=150, width=180, height=80, color="orange")

# Event label
arch.text_box(230, 175, "OrderCreated", font_size=14, color="orange")

# Consumer services (right side)
arch.service("inventory", "Inventory Service\n(reserves stock)", x=700, y=80, color="violet")
arch.service("notification", "Notification Service\n(sends email)", x=700, y=200, color="violet")
arch.service("analytics", "Analytics Service\n(tracks metrics)", x=700, y=320, color="violet")
arch.service("shipping", "Shipping Service\n(prepares label)", x=700, y=440, color="violet")

# Connections - Order to Event Bus
arch.connect("order_service", "event_bus", "publish")

# Event Bus to Consumers
arch.connect("event_bus", "inventory", "subscribe")
arch.connect("event_bus", "notification", "subscribe")
arch.connect("event_bus", "analytics", "subscribe")
arch.connect("event_bus", "shipping", "subscribe")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/event_driven.excalidraw"
arch.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(arch.elements)}")
