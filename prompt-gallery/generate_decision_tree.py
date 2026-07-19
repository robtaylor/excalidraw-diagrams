#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a decision tree flowchart for support ticket routing
fc = Flowchart(direction="vertical", spacing=100)

fc.start("New Ticket")
fc.decision("urgent", "Is it urgent?")

# Urgent path
fc.position_at(100, 340)
fc.process("priority", "Priority Queue")

# Not urgent - continue decision tree
fc.position_at(400, 340)
fc.decision("billing", "Is it billing related?")

# Billing team
fc.position_at(250, 540)
fc.process("billing_team", "Billing Team")

# Not billing - check technical
fc.position_at(500, 540)
fc.decision("technical", "Is it technical?")

# Not technical - general support
fc.position_at(350, 740)
fc.process("general", "General Support")

# Technical - check complexity
fc.position_at(600, 740)
fc.decision("complexity", "Simple issue?")

# Simple - Tier 1
fc.position_at(500, 940)
fc.process("tier1", "Tier 1 Support")

# Complex - Tier 2
fc.position_at(700, 940)
fc.process("tier2", "Tier 2 Support")

# Connections
fc.connect("__start__", "urgent")
fc.connect("urgent", "priority", "Yes")
fc.connect("urgent", "billing", "No")
fc.connect("billing", "billing_team", "Yes")
fc.connect("billing", "technical", "No")
fc.connect("technical", "general", "No")
fc.connect("technical", "complexity", "Yes")
fc.connect("complexity", "tier1", "Yes")
fc.connect("complexity", "tier2", "No")

fc.save("gallery_output/decision_tree.excalidraw")
print("Created: decision_tree.excalidraw")
