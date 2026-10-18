#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a state machine diagram for an e-commerce order (horizontal layout)
d = Diagram()

# Title
d.text_box(50, 30, "E-commerce Order State Machine", font_size=24, color="black")

# States (horizontal layout)
created = d.box(50, 100, "Created", color="blue", shape="rectangle")
pending = d.box(250, 100, "Pending\nPayment", color="yellow", shape="rectangle")
paid = d.box(450, 100, "Paid", color="green", shape="rectangle")
processing = d.box(650, 100, "Processing", color="blue", shape="rectangle")
shipped = d.box(850, 100, "Shipped", color="blue", shape="rectangle")
delivered = d.box(1050, 100, "Delivered", color="green", shape="rectangle")

# Cancelled and Refunded states (below)
cancelled = d.box(450, 280, "Cancelled", color="red", shape="rectangle")
refunded = d.box(850, 280, "Refunded", color="orange", shape="rectangle")

# Transitions (forward flow)
d.arrow_between(created, pending, "order_created")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "items_packed")
d.arrow_between(processing, shipped, "shipped")
d.arrow_between(shipped, delivered, "delivered")

# Cancellation paths
d.arrow_between(pending, cancelled, "cancel_requested")
d.arrow_between(paid, cancelled, "cancel_requested")
d.arrow_between(processing, cancelled, "cancel_requested")

# Refund path
d.arrow_between(cancelled, refunded, "refund_approved")
d.arrow_between(delivered, refunded, "refund_approved")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/state_machine.excalidraw"
d.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(d.elements)}")
