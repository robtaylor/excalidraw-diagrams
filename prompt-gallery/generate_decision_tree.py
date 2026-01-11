#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create support ticket routing decision tree
fc = Flowchart(direction="vertical", spacing=100)

fc.start("New Ticket")
fc.decision("urgent", "Is it urgent?")

# Urgent path
fc.position_at(150, 280)
fc.process("priority_queue", "Priority Queue")

# Not urgent, continue with routing
fc.position_at(450, 280)
fc.decision("billing", "Is it billing related?")

# Billing related
fc.position_at(650, 420)
fc.process("billing_team", "Billing Team")

# Not billing, check technical
fc.position_at(450, 520)
fc.decision("technical", "Is it technical?")

# Not technical - general support
fc.position_at(650, 660)
fc.process("general_support", "General Support")

# Technical, check complexity
fc.position_at(450, 760)
fc.decision("complexity", "Simple issue?")

# Simple - Tier 1
fc.position_at(300, 900)
fc.process("tier1", "Tier 1 Support")

# Complex - Tier 2
fc.position_at(600, 900)
fc.process("tier2", "Tier 2 Support")

# Connections
fc.connect("__start__", "urgent")
fc.connect("urgent", "priority_queue", "Yes")
fc.connect("urgent", "billing", "No")
fc.connect("billing", "billing_team", "Yes")
fc.connect("billing", "technical", "No")
fc.connect("technical", "general_support", "No")
fc.connect("technical", "complexity", "Yes")
fc.connect("complexity", "tier1", "Yes")
fc.connect("complexity", "tier2", "No")

fc.save("gallery_output/decision_tree.excalidraw")
print("✓ Created: gallery_output/decision_tree.excalidraw")
