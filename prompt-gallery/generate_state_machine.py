#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# State machine for e-commerce order - horizontal layout
d = Diagram()

# States in horizontal layout
created = d.box(50, 200, "Created", color="blue", shape="ellipse")
pending = d.box(220, 200, "Pending\nPayment", color="yellow", shape="ellipse")
paid = d.box(390, 200, "Paid", color="green", shape="ellipse")
processing = d.box(560, 200, "Processing", color="blue", shape="ellipse")
shipped = d.box(730, 200, "Shipped", color="cyan", shape="ellipse")
delivered = d.box(900, 200, "Delivered", color="green", shape="ellipse")

# Alternative states below
cancelled = d.box(390, 380, "Cancelled", color="red", shape="ellipse")
refunded = d.box(730, 380, "Refunded", color="orange", shape="ellipse")

# Main flow transitions
d.arrow_between(created, pending, "submit")
d.arrow_between(pending, paid, "payment_received")
d.arrow_between(paid, processing, "start_processing")
d.arrow_between(processing, shipped, "items_packed")
d.arrow_between(shipped, delivered, "delivered")

# Cancellation paths
d.arrow_between(created, cancelled, "cancel_requested")
d.arrow_between(pending, cancelled, "cancel_requested")
d.arrow_between(paid, cancelled, "cancel_approved")

# Refund path
d.arrow_between(cancelled, refunded, "refund_approved")
d.arrow_between(delivered, refunded, "return_approved")

d.save("gallery_output/state_machine.excalidraw")
print("Created: gallery_output/state_machine.excalidraw")
