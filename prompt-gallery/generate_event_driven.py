#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Create event-driven architecture diagram
arch = ArchitectureDiagram()

# Add title
arch.text_box(250, 30, "Event-Driven Architecture", font_size=24)

# Order Service (publisher)
order_svc = arch.service("order", "Order Service", x=100, y=150, color="blue")

# Event Bus (center)
event_bus = arch.component("eventbus", "Event Bus\n(Kafka/SNS)", x=350, y=200,
                          width=180, height=100, color="orange")

# Event label
arch.text_box(200, 230, "OrderCreated", font_size=16, color="orange")

# Consumer services (right side, arranged vertically)
inventory = arch.service("inventory", "Inventory Service\n(reserves stock)",
                        x=650, y=100, color="violet")
notification = arch.service("notification", "Notification Service\n(sends email)",
                           x=650, y=200, color="violet")
analytics = arch.service("analytics", "Analytics Service\n(tracks metrics)",
                        x=650, y=300, color="violet")
shipping = arch.service("shipping", "Shipping Service\n(prepares label)",
                       x=650, y=400, color="violet")

# Connections
# Order Service publishes to Event Bus
arch.connect("order", "eventbus", "publishes")

# Event Bus to all consumers
arch.connect("eventbus", "inventory", "subscribes")
arch.connect("eventbus", "notification", "subscribes")
arch.connect("eventbus", "analytics", "subscribes")
arch.connect("eventbus", "shipping", "subscribes")

arch.save("gallery_output/event_driven.excalidraw")
print("Created: gallery_output/event_driven.excalidraw")
