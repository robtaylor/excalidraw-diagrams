#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create an event-driven architecture diagram
arch = ArchitectureDiagram()

# Title
arch.text_box(240, 20, "Event-Driven Architecture", font_size=28)

# Publisher
arch.service("order_service", "Order Service", x=100, y=100, color="blue")

# Event
arch.component("event", "OrderCreated\nEvent", x=350, y=100, color="yellow", width=150, height=80)

# Event Bus
arch.component("event_bus", "Event Bus\n(Kafka/SNS)", x=320, y=240, color="orange", width=200, height=80)

# Consumers
arch.service("inventory", "Inventory Service\n(reserves stock)", x=100, y=400, color="green")
arch.service("notification", "Notification Service\n(sends email)", x=300, y=400, color="green")
arch.service("analytics", "Analytics Service\n(tracks metrics)", x=520, y=400, color="green")
arch.service("shipping", "Shipping Service\n(prepares label)", x=720, y=400, color="green")

# Connections
arch.connect("order_service", "event", "publishes")
arch.connect("event", "event_bus", "to")
arch.connect("event_bus", "inventory", "consumes")
arch.connect("event_bus", "notification", "consumes")
arch.connect("event_bus", "analytics", "consumes")
arch.connect("event_bus", "shipping", "consumes")

arch.save("gallery_output/event_driven.excalidraw")
print("Created: gallery_output/event_driven.excalidraw")
