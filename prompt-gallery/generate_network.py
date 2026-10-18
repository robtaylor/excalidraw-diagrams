#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a network architecture diagram
d = Diagram()

# Title
d.text_box(300, 30, "Cloud VPC Network Architecture", font_size=24, color="black")

# Internet
internet = d.box(400, 100, "Internet", width=150, height=60, color="gray", shape="ellipse")

# Load Balancer
lb = d.box(375, 220, "Load Balancer", width=200, height=70, color="blue")

# VPC boundary (large rectangle) - create with text box border
d.text_box(50, 300, "VPC", font_size=20, color="black")

# Public Subnet boundary
d.text_box(80, 340, "Public Subnet", font_size=16, color="blue")
nat = d.box(100, 380, "NAT Gateway", width=160, height=60, color="cyan")
bastion = d.box(300, 380, "Bastion Host", width=160, height=60, color="cyan")

# Private Subnet boundary
d.text_box(80, 490, "Private Subnet", font_size=16, color="green")
web1 = d.box(100, 530, "Web Server 1", width=160, height=60, color="blue")
web2 = d.box(300, 530, "Web Server 2", width=160, height=60, color="blue")
app1 = d.box(100, 630, "App Server 1", width=160, height=60, color="violet")
app2 = d.box(300, 630, "App Server 2", width=160, height=60, color="violet")

# Database Subnet boundary
d.text_box(550, 490, "Database Subnet", font_size=16, color="red")
primary_db = d.box(570, 530, "Primary DB", width=160, height=60, color="green")
replica_db = d.box(570, 630, "Read Replica", width=160, height=60, color="green")

# Connections
d.arrow_between(internet, lb, "HTTPS")
d.arrow_between(lb, web1)
d.arrow_between(lb, web2)
d.arrow_between(web1, app1)
d.arrow_between(web2, app2)
d.arrow_between(app1, primary_db, "SQL")
d.arrow_between(app2, primary_db, "SQL")
d.arrow_between(primary_db, replica_db, "replication")

# NAT gateway connections
d.arrow_between(nat, internet, "outbound")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/network_topology.excalidraw"
d.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(d.elements)}")
