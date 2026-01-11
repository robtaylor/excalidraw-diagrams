#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create network architecture diagram
d = Diagram()

# Title
d.text_box(350, 30, "Cloud VPC Network Architecture", font_size=24)

# Internet
internet = d.box(380, 100, "Internet", color="cyan", shape="ellipse", width=120, height=60)

# VPC boundary (large rectangle in background)
d.text_box(100, 180, "VPC", font_size=20, color="blue")

# Load Balancer
lb = d.box(360, 220, "Load Balancer", color="violet", width=140, height=60)

# Public Subnet boundary
d.text_box(120, 320, "Public Subnet", font_size=16, color="green")
nat = d.box(150, 360, "NAT Gateway", color="orange", width=130, height=60)
bastion = d.box(320, 360, "Bastion Host", color="orange", width=130, height=60)

# Private Subnet boundary
d.text_box(120, 480, "Private Subnet", font_size=16, color="green")
web1 = d.box(120, 520, "Web Server", color="blue", width=120, height=60)
web2 = d.box(260, 520, "Web Server", color="blue", width=120, height=60)
app1 = d.box(420, 520, "App Server", color="blue", width=120, height=60)
app2 = d.box(560, 520, "App Server", color="blue", width=120, height=60)

# Database Subnet boundary
d.text_box(120, 640, "Database Subnet", font_size=16, color="green")
primary_db = d.box(200, 680, "Primary DB", color="green", width=130, height=60)
replica_db = d.box(400, 680, "Read Replica", color="teal", width=130, height=60)

# Connections
d.arrow_between(internet, lb, "HTTPS")
d.arrow_between(lb, web1, "")
d.arrow_between(lb, web2, "")
d.arrow_between(web1, app1, "")
d.arrow_between(web2, app2, "")
d.arrow_between(app1, primary_db, "SQL")
d.arrow_between(app2, primary_db, "SQL")
d.arrow_between(primary_db, replica_db, "replication")

d.save("gallery_output/network_topology.excalidraw")
print("✓ Created: gallery_output/network_topology.excalidraw")
