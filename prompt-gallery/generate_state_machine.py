#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create state machine diagram with horizontal layout
d = Diagram()

# Title
d.text_box(300, 30, "Order State Machine", font_size=24)

# States in horizontal layout
created = d.box(50, 150, "Created", color="blue", shape="ellipse", width=120, height=80)
pending = d.box(220, 150, "Pending\nPayment", color="yellow", shape="ellipse", width=120, height=80)
paid = d.box(390, 150, "Paid", color="green", shape="ellipse", width=120, height=80)
processing = d.box(560, 150, "Processing", color="blue", shape="ellipse", width=120, height=80)
shipped = d.box(730, 150, "Shipped", color="blue", shape="ellipse", width=120, height=80)
delivered = d.box(900, 150, "Delivered", color="green", shape="ellipse", width=120, height=80)

# Alternative states below
cancelled = d.box(300, 320, "Cancelled", color="red", shape="ellipse", width=120, height=80)
refunded = d.box(650, 320, "Refunded", color="orange", shape="ellipse", width=120, height=80)

# Main flow transitions
d.arrow_between(created, pending, "order_created")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "start_processing")
d.arrow_between(processing, shipped, "items_packed")
d.arrow_between(shipped, delivered, "delivered")

# Cancel transitions
d.arrow_between(created, cancelled, "cancel_requested", from_side="bottom", to_side="left")
d.arrow_between(pending, cancelled, "cancel_requested", from_side="bottom", to_side="top")
d.arrow_between(paid, cancelled, "cancel_requested", from_side="bottom", to_side="top")

# Refund transitions
d.arrow_between(delivered, refunded, "refund_approved", from_side="bottom", to_side="right")

d.save("gallery_output/state_machine.excalidraw")
print("✓ Created: gallery_output/state_machine.excalidraw")
