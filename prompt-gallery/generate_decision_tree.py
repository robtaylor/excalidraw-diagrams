#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Support Ticket Routing Decision Tree
fc = Flowchart(direction="vertical", spacing=100)

fc.start("New Ticket")
fc.decision("urgent", "Is it urgent?")

# Urgent path
fc.position_at(100, 280)
fc.process("priority", "Priority Queue")

# Not urgent - continue triage
fc.position_at(400, 280)
fc.decision("billing", "Is it billing\nrelated?")

# Billing path
fc.position_at(250, 440)
fc.process("billing_team", "Billing Team")

# Not billing - check technical
fc.position_at(550, 440)
fc.decision("technical", "Is it\ntechnical?")

# Not technical
fc.position_at(400, 600)
fc.process("general", "General Support")

# Technical - check complexity
fc.position_at(700, 600)
fc.decision("simple", "Simple issue?")

# Simple technical
fc.position_at(600, 760)
fc.process("tier1", "Tier 1 Support")

# Complex technical
fc.position_at(800, 760)
fc.process("tier2", "Tier 2 Support")

# Connections
fc.connect("__start__", "urgent")

# Urgent branch
fc.connect("urgent", "priority", "Yes")

# Not urgent branch
fc.connect("urgent", "billing", "No")

# Billing branch
fc.connect("billing", "billing_team", "Yes")

# Not billing
fc.connect("billing", "technical", "No")

# Not technical
fc.connect("technical", "general", "No")

# Technical - check complexity
fc.connect("technical", "simple", "Yes")

# Simple vs complex
fc.connect("simple", "tier1", "Yes")
fc.connect("simple", "tier2", "No")

fc.save("gallery_output/decision_tree.excalidraw")
print("Created: gallery_output/decision_tree.excalidraw")
