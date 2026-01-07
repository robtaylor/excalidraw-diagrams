#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create state machine diagram with horizontal layout
d = Diagram()

# Add title
d.text_box(50, 30, "Order State Machine", font_size=24)

# States arranged horizontally with multiple rows
# Row 1: Initial states
created = d.box(50, 100, "Created", color="gray", shape="ellipse")
pending = d.box(250, 100, "Pending\nPayment", color="yellow", shape="ellipse")
paid = d.box(450, 100, "Paid", color="green", shape="ellipse")
processing = d.box(650, 100, "Processing", color="blue", shape="ellipse")

# Row 2: Completion states
shipped = d.box(250, 280, "Shipped", color="blue", shape="ellipse")
delivered = d.box(450, 280, "Delivered", color="green", shape="ellipse")

# Row 3: Error states
cancelled = d.box(50, 280, "Cancelled", color="red", shape="ellipse")
refunded = d.box(650, 280, "Refunded", color="orange", shape="ellipse")

# Transitions - main flow
d.arrow_between(created, pending, "order_created")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "payment_confirmed")
d.arrow_between(processing, shipped, "items_packed")
d.arrow_between(shipped, delivered, "delivered")

# Cancel paths
d.arrow_between(created, cancelled, "cancel_requested")
d.arrow_between(pending, cancelled, "cancel_requested")
d.arrow_between(paid, cancelled, "cancel_requested")

# Refund path
d.arrow_between(cancelled, refunded, "refund_approved")
d.arrow_between(delivered, refunded, "refund_approved")

d.save("gallery_output/state_machine.excalidraw")
print("Created: gallery_output/state_machine.excalidraw")
