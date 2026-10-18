#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a decision tree for support ticket routing
fc = Flowchart(direction="vertical", spacing=100)

# Start
fc.start("New Ticket")

# First decision - Urgent?
fc.decision("urgent", "Is it urgent?")

# Urgent Yes path
fc.position_at(100, 240)
fc.process("priority_queue", "Priority Queue")

# Urgent No path - continue main flow
fc.position_at(400, 240)
fc.decision("billing", "Billing related?")

# Billing Yes
fc.position_at(200, 380)
fc.process("billing_team", "Billing Team")

# Billing No - check technical
fc.position_at(500, 380)
fc.decision("technical", "Is it technical?")

# Not technical
fc.position_at(300, 520)
fc.process("general", "General Support")

# Technical Yes - check complexity
fc.position_at(650, 520)
fc.decision("complexity", "Simple issue?")

# Simple
fc.position_at(550, 660)
fc.process("tier1", "Tier 1 Support")

# Complex
fc.position_at(750, 660)
fc.process("tier2", "Tier 2 Support")

# Connections
fc.connect("__start__", "urgent")
fc.connect("urgent", "priority_queue", "Yes")
fc.connect("urgent", "billing", "No")
fc.connect("billing", "billing_team", "Yes")
fc.connect("billing", "technical", "No")
fc.connect("technical", "general", "No")
fc.connect("technical", "complexity", "Yes")
fc.connect("complexity", "tier1", "Yes")
fc.connect("complexity", "tier2", "No")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/decision_tree.excalidraw"
fc.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(fc.elements)}")
