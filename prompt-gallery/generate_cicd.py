#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a CI/CD pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

# Start
fc.start("Developer Pushes Code")

# GitHub triggers
fc.process("trigger", "GitHub Triggers Workflow")

# Run tests
fc.process("tests", "Run Tests")
fc.decision("test_result", "Tests Pass?")

# Fail path
fc.position_at(100, 440)
fc.process("notify_fail", "Notify Developer")
fc.end("Stop")

# Success path - continue from test_result
fc.position_at(500, 440)
fc.process("build", "Build Docker Image")
fc.process("push", "Push to Registry")
fc.process("deploy_staging", "Deploy to Staging")
fc.process("e2e", "Run E2E Tests")
fc.decision("e2e_result", "E2E Pass?")

# E2E fail - position
fc.position_at(300, 900)
fc.process("notify_e2e_fail", "Notify Developer")

# E2E success - position
fc.position_at(500, 980)
fc.process("deploy_prod", "Deploy to Production")
fc.process("success_notify", "Send Success Notification")

# Connections
fc.connect("__start__", "trigger")
fc.connect("trigger", "tests")
fc.connect("tests", "test_result")
fc.connect("test_result", "notify_fail", "Fail")
fc.connect("notify_fail", "__end__")
fc.connect("test_result", "build", "Pass")
fc.connect("build", "push")
fc.connect("push", "deploy_staging")
fc.connect("deploy_staging", "e2e")
fc.connect("e2e", "e2e_result")
fc.connect("e2e_result", "notify_e2e_fail", "Fail")
fc.connect("e2e_result", "deploy_prod", "Pass")
fc.connect("deploy_prod", "success_notify")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/cicd_pipeline.excalidraw"
fc.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(fc.elements)}")
