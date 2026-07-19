#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a network architecture diagram
d = Diagram()

# Title
d.text_box(350, 30, "Cloud VPC Network Architecture", font_size=24)

# VPC boundary (large box)
d.text_box(50, 90, "VPC", font_size=20, color="gray")

# Internet
internet = d.box(350, 100, "Internet", color="gray", width=150)

# Load Balancer
lb = d.box(350, 220, "Load Balancer", color="violet", width=150)

# Public Subnet box
d.text_box(80, 330, "Public Subnet", font_size=16, color="blue")
nat = d.box(100, 370, "NAT Gateway", color="orange", width=130)
bastion = d.box(280, 370, "Bastion Host", color="orange", width=130)

# Private Subnet box
d.text_box(480, 330, "Private Subnet", font_size=16, color="green")
web1 = d.box(480, 370, "Web Server 1", color="blue", width=130)
web2 = d.box(480, 470, "Web Server 2", color="blue", width=130)
app1 = d.box(660, 370, "App Server 1", color="cyan", width=130)
app2 = d.box(660, 470, "App Server 2", color="cyan", width=130)

# Database Subnet box
d.text_box(280, 570, "Database Subnet", font_size=16, color="red")
primary_db = d.box(250, 610, "Primary DB", color="green", width=130)
replica_db = d.box(450, 610, "Read Replica", color="green", width=130)

# Connections
d.arrow_between(internet, lb, "HTTPS")
d.arrow_between(lb, web1, "")
d.arrow_between(lb, web2, "")
d.arrow_between(web1, app1, "")
d.arrow_between(web2, app2, "")
d.arrow_between(app1, primary_db, "SQL")
d.arrow_between(app2, primary_db, "SQL")
d.arrow_between(primary_db, replica_db, "replication")
d.arrow_between(bastion, web1, "SSH")
d.arrow_between(nat, internet, "egress")

d.save("gallery_output/network_topology.excalidraw")
print("Created: network_topology.excalidraw")
