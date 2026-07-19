#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a state machine diagram with horizontal layout
d = Diagram()

# Title
d.text_box(300, 30, "Order State Machine", font_size=24)

# States - horizontal layout in rows
created = d.box(100, 120, "Created", color="gray", shape="ellipse")
pending = d.box(300, 120, "Pending Payment", color="yellow", shape="ellipse")
paid = d.box(520, 120, "Paid", color="green", shape="ellipse")
processing = d.box(720, 120, "Processing", color="blue", shape="ellipse")

shipped = d.box(100, 280, "Shipped", color="blue", shape="ellipse")
delivered = d.box(300, 280, "Delivered", color="green", shape="ellipse")
cancelled = d.box(520, 280, "Cancelled", color="red", shape="ellipse")
refunded = d.box(720, 280, "Refunded", color="orange", shape="ellipse")

# State transitions
d.arrow_between(created, pending, "init")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "items_packed")
d.arrow_between(processing, shipped, "shipped")
d.arrow_between(shipped, delivered, "delivered")

# Cancel paths
d.arrow_between(created, cancelled, "cancel_requested")
d.arrow_between(pending, cancelled, "cancel_requested")
d.arrow_between(paid, cancelled, "cancel_requested")

# Refund path
d.arrow_between(cancelled, refunded, "refund_approved")
d.arrow_between(delivered, refunded, "refund_approved")

d.save("gallery_output/state_machine.excalidraw")
print("Created: state_machine.excalidraw")
