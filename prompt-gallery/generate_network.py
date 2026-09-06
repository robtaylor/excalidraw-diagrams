#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Cloud VPC Network Architecture
d = Diagram()

# Internet
internet = d.box(400, 50, "Internet", color="gray", width=120)

# Load Balancer
lb = d.box(380, 160, "Load Balancer", color="orange", width=160)

# VPC boundary (large container concept - using text labels)
d.text_box(80, 250, "VPC", font_size=22, color="blue")

# Public Subnet
d.text_box(100, 290, "Public Subnet", font_size=18, color="cyan")
nat = d.box(120, 340, "NAT Gateway", color="cyan", width=140)
bastion = d.box(320, 340, "Bastion Host", color="cyan", width=140)

# Private Subnet
d.text_box(100, 450, "Private Subnet", font_size=18, color="violet")
web1 = d.box(120, 500, "Web Server 1", color="violet", width=140)
web2 = d.box(120, 600, "Web Server 2", color="violet", width=140)
app1 = d.box(320, 500, "App Server 1", color="violet", width=140)
app2 = d.box(320, 600, "App Server 2", color="violet", width=140)

# Database Subnet
d.text_box(550, 450, "Database Subnet", font_size=18, color="green")
primary_db = d.box(560, 500, "Primary DB", color="green", width=140)
replica_db = d.box(560, 600, "Read Replica", color="green", width=140)

# Connections
d.arrow_between(internet, lb)
d.arrow_between(lb, bastion)
d.arrow_between(lb, web1)
d.arrow_between(lb, web2)

d.arrow_between(web1, app1)
d.arrow_between(web2, app1)
d.arrow_between(web1, app2)
d.arrow_between(web2, app2)

d.arrow_between(app1, primary_db)
d.arrow_between(app2, primary_db)
d.arrow_between(app1, replica_db)
d.arrow_between(app2, replica_db)

# NAT for outbound traffic
d.arrow_between(app1, nat, from_side="left", to_side="bottom")

d.save("gallery_output/network_topology.excalidraw")
print("Created: gallery_output/network_topology.excalidraw")
