#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create event-driven architecture
arch = ArchitectureDiagram()

# Title
arch.text_box(300, 30, "Event-Driven Architecture", font_size=24)

# Order Service (publisher)
arch.service("order_service", "Order Service", x=100, y=120, color="blue")

# Event created
event = arch.component("event", "OrderCreated\nEvent", x=100, y=250, color="yellow", width=140, height=80)

# Event Bus
arch.component("event_bus", "Event Bus\n(Kafka/SNS)", x=340, y=220, color="violet", width=160, height=100)

# Consumer services (spread out horizontally)
arch.service("inventory", "Inventory Service\n(reserves stock)", x=100, y=400, color="green")
arch.service("notification", "Notification Service\n(sends email)", x=300, y=400, color="orange")
arch.service("analytics", "Analytics Service\n(tracks metrics)", x=500, y=400, color="teal")
arch.service("shipping", "Shipping Service\n(prepares label)", x=700, y=400, color="cyan")

# Connections
arch.connect("order_service", "event", "publishes")
arch.connect("event", "event_bus", "")
arch.connect("event_bus", "inventory", "consume")
arch.connect("event_bus", "notification", "consume")
arch.connect("event_bus", "analytics", "consume")
arch.connect("event_bus", "shipping", "consume")

arch.save("gallery_output/event_driven.excalidraw")
print("✓ Created: gallery_output/event_driven.excalidraw")
