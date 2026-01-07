#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create decision tree for support ticket routing
fc = Flowchart(direction="vertical", spacing=100)

fc.start("New Ticket")
fc.decision("urgent", "Is it urgent?")

# Urgent path - goes to Priority Queue
fc.position_at(100, 340)
fc.process("priority", "Priority Queue")

# Not urgent - continue with routing
fc.position_at(400, 340)
fc.decision("billing", "Is it billing related?")

# Billing path
fc.position_at(200, 540)
fc.process("billing_team", "Billing Team")

# Not billing - check if technical
fc.position_at(500, 540)
fc.decision("technical", "Is it technical?")

# Not technical - General Support
fc.position_at(350, 740)
fc.process("general", "General Support")

# Technical - check complexity
fc.position_at(650, 740)
fc.decision("complex", "Simple issue?")

# Simple - Tier 1
fc.position_at(550, 940)
fc.process("tier1", "Tier 1 Support")

# Complex - Tier 2
fc.position_at(750, 940)
fc.process("tier2", "Tier 2 Support")

# Connections
fc.connect("__start__", "urgent")
fc.connect("urgent", "priority", "Yes")
fc.connect("urgent", "billing", "No")
fc.connect("billing", "billing_team", "Yes")
fc.connect("billing", "technical", "No")
fc.connect("technical", "general", "No")
fc.connect("technical", "complex", "Yes")
fc.connect("complex", "tier1", "Yes")
fc.connect("complex", "tier2", "No")

fc.save("gallery_output/decision_tree.excalidraw")
print("Created: gallery_output/decision_tree.excalidraw")
