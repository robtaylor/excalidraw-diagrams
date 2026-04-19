#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a network architecture diagram
d = Diagram()

# Title
d.text_box(280, 20, "VPC Network Architecture", font_size=28)

# Internet
internet = d.box(350, 80, "Internet", color="cyan", shape="ellipse", width=120)

# Load Balancer
lb = d.box(330, 180, "Load Balancer", color="violet", width=160)

# VPC boundary (large rectangle - we'll draw this manually with text)
d.text_box(50, 260, "VPC Boundary", font_size=16, color="gray")

# Public Subnet area
d.text_box(70, 300, "Public Subnet", font_size=16, color="blue")
nat = d.box(80, 340, "NAT Gateway", color="blue", width=140)
bastion = d.box(260, 340, "Bastion Host", color="blue", width=140)

# Private Subnet area
d.text_box(70, 460, "Private Subnet", font_size=16, color="green")
web1 = d.box(80, 500, "Web Server 1", color="green", width=140)
web2 = d.box(260, 500, "Web Server 2", color="green", width=140)
app1 = d.box(440, 500, "App Server 1", color="green", width=140)
app2 = d.box(620, 500, "App Server 2", color="green", width=140)

# Database Subnet area
d.text_box(70, 620, "Database Subnet", font_size=16, color="orange")
primary_db = d.box(200, 660, "Primary DB", color="orange", width=140, shape="ellipse")
replica_db = d.box(420, 660, "Read Replica", color="orange", width=140, shape="ellipse")

# Connections
d.arrow_between(internet, lb, "HTTPS")
d.arrow_between(lb, web1)
d.arrow_between(lb, web2)
d.arrow_between(web1, app1)
d.arrow_between(web2, app2)
d.arrow_between(app1, primary_db, "SQL")
d.arrow_between(app2, primary_db, "SQL")
d.arrow_between(primary_db, replica_db, "replication")
d.arrow_between(bastion, web1, "SSH")
d.arrow_between(nat, internet, from_side="top", to_side="bottom")

d.save("gallery_output/network_topology.excalidraw")
print("Created: gallery_output/network_topology.excalidraw")
