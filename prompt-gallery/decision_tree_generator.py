#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a decision tree flowchart for support ticket routing
fc = Flowchart(direction="vertical", spacing=90)

fc.start("New Ticket")
fc.decision("urgent", "Is it Urgent?")

# Urgent path (right branch)
fc.position_at(450, 210)
fc.process("priority", "Priority Queue")

# Not urgent, continue checks (left branch)
fc.position_at(150, 210)
fc.decision("billing", "Is it Billing\nRelated?")

# Billing related (right branch from billing)
fc.position_at(250, 360)
fc.process("billing_team", "Billing Team")

# Not billing, check technical (left branch)
fc.position_at(50, 360)
fc.decision("technical", "Is it Technical?")

# Not technical
fc.position_at(150, 510)
fc.process("general", "General Support")

# Technical - check complexity (bottom from technical)
fc.position_at(50, 510)
fc.decision("complexity", "Simple Issue?")

# Simple technical
fc.position_at(150, 660)
fc.process("tier1", "Tier 1 Support")

# Complex technical
fc.position_at(50, 660)
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
print("Created: gallery_output/decision_tree.excalidraw")
