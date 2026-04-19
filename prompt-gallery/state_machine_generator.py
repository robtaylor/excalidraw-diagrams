#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a state machine diagram with horizontal layout
d = Diagram()

# Title
d.text_box(50, 30, "Order State Machine", font_size=24)

# States - horizontal layout
created = d.box(50, 100, "Created", color="cyan", shape="ellipse")
pending = d.box(200, 100, "Pending\nPayment", color="yellow", shape="ellipse")
paid = d.box(370, 100, "Paid", color="green", shape="ellipse")
processing = d.box(520, 100, "Processing", color="blue", shape="ellipse")
shipped = d.box(50, 280, "Shipped", color="blue", shape="ellipse")
delivered = d.box(220, 280, "Delivered", color="green", shape="ellipse")
cancelled = d.box(400, 280, "Cancelled", color="red", shape="ellipse")
refunded = d.box(570, 280, "Refunded", color="orange", shape="ellipse")

# Main flow transitions
d.arrow_between(created, pending, "created")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "items_packed")
d.arrow_between(processing, shipped, "shipped")
d.arrow_between(shipped, delivered, "delivered")

# Cancel transitions
d.arrow_between(created, cancelled, "cancel_requested", from_side="bottom", to_side="left")
d.arrow_between(pending, cancelled, "cancel_requested", from_side="bottom", to_side="top")
d.arrow_between(paid, cancelled, "cancel_requested", from_side="bottom", to_side="top")

# Refund transitions
d.arrow_between(paid, refunded, "refund_approved", from_side="bottom", to_side="left")
d.arrow_between(processing, refunded, "refund_approved", from_side="bottom", to_side="left")
d.arrow_between(delivered, refunded, "refund_approved", from_side="right", to_side="top")

d.save("gallery_output/state_machine.excalidraw")
print("Created: gallery_output/state_machine.excalidraw")
