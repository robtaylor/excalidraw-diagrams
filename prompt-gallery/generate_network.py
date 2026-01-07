#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create network architecture diagram
d = Diagram()

# Add title
d.text_box(280, 30, "Cloud VPC Network Architecture", font_size=24)

# VPC boundary - large rectangle
d.text_box(50, 80, "VPC", font_size=20, color="blue")

# Internet
internet = d.box(350, 120, "Internet", width=140, height=60, color="gray")

# Load Balancer
lb = d.box(350, 230, "Load Balancer", width=160, height=60, color="violet")

# Public Subnet
d.text_box(120, 330, "Public Subnet", font_size=18, color="cyan")
nat = d.box(100, 370, "NAT Gateway", width=140, height=60, color="cyan")
bastion = d.box(280, 370, "Bastion Host", width=140, height=60, color="cyan")

# Private Subnet
d.text_box(520, 330, "Private Subnet", font_size=18, color="blue")
web1 = d.box(480, 370, "Web Server 1", width=140, height=60, color="blue")
web2 = d.box(480, 450, "Web Server 2", width=140, height=60, color="blue")
app1 = d.box(660, 370, "App Server 1", width=140, height=60, color="blue")
app2 = d.box(660, 450, "App Server 2", width=140, height=60, color="blue")

# Database Subnet
d.text_box(340, 560, "Database Subnet", font_size=18, color="green")
primary_db = d.box(300, 600, "Primary DB", width=140, height=60, color="green")
replica_db = d.box(480, 600, "Read Replica", width=140, height=60, color="green")

# Connections
d.arrow_between(internet, lb, "HTTPS")
d.arrow_between(lb, bastion)
d.arrow_between(lb, web1)
d.arrow_between(lb, web2)
d.arrow_between(web1, app1)
d.arrow_between(web2, app1)
d.arrow_between(web1, app2)
d.arrow_between(web2, app2)
d.arrow_between(app1, primary_db, "SQL")
d.arrow_between(app2, primary_db, "SQL")
d.arrow_between(app1, replica_db, "Read")
d.arrow_between(app2, replica_db, "Read")
d.arrow_between(primary_db, replica_db, "Replication")
d.arrow_between(nat, internet, "Outbound")

d.save("gallery_output/network_topology.excalidraw")
print("Created: gallery_output/network_topology.excalidraw")
