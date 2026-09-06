#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import ArchitectureDiagram

# Event-Driven Architecture
arch = ArchitectureDiagram()

# Order Service (publisher)
arch.service("order_svc", "Order Service", x=350, y=80, color="blue")

# Event published
arch.component("event", "OrderCreated\nEvent", x=335, y=220, width=130, height=60, color="yellow")

# Event Bus
arch.component("event_bus", "Event Bus\n(Kafka/SNS)", x=320, y=360, width=160, height=80, color="orange")

# Consumer services
arch.service("inventory", "Inventory Service\n(reserves stock)", x=80, y=520, color="violet")
arch.service("notification", "Notification Service\n(sends email)", x=280, y=520, color="violet")
arch.service("analytics", "Analytics Service\n(tracks metrics)", x=480, y=520, color="violet")
arch.service("shipping", "Shipping Service\n(prepares label)", x=680, y=520, color="violet")

# Connections - Order service publishes event
arch.connect("order_svc", "event", "publishes")
arch.connect("event", "event_bus", "")

# Event bus to consumers
arch.connect("event_bus", "inventory", "subscribe")
arch.connect("event_bus", "notification", "subscribe")
arch.connect("event_bus", "analytics", "subscribe")
arch.connect("event_bus", "shipping", "subscribe")

arch.save("gallery_output/event_driven.excalidraw")
print("Created: gallery_output/event_driven.excalidraw")
