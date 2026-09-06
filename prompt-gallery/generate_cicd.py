#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# CI/CD Pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

# Start
fc.start("Developer Pushes Code")

# Main flow
fc.process("trigger", "GitHub Triggers Workflow")
fc.process("test", "Run Tests")
fc.decision("test_pass", "Tests Pass?")

# Failure path
fc.position_at(100, 540)
fc.process("notify_fail", "Notify Developer")
fc.end("Stop")

# Success path
fc.position_at(400, 540)
fc.process("build", "Build Docker Image")
fc.process("push", "Push to Registry")
fc.process("deploy_stage", "Deploy to Staging")
fc.process("e2e", "Run E2E Tests")
fc.decision("e2e_pass", "E2E Pass?")

# E2E failure
fc.position_at(250, 1140)
fc.process("notify_e2e_fail", "Notify Developer")

# E2E success
fc.position_at(550, 1140)
fc.process("deploy_prod", "Deploy to Production")
fc.process("notify_success", "Send Success Notification")

# Connections
fc.connect("__start__", "trigger")
fc.connect("trigger", "test")
fc.connect("test", "test_pass")

# Test failure branch
fc.connect("test_pass", "notify_fail", "Fail")
fc.connect("notify_fail", "__end__")

# Test success branch
fc.connect("test_pass", "build", "Pass")
fc.connect("build", "push")
fc.connect("push", "deploy_stage")
fc.connect("deploy_stage", "e2e")
fc.connect("e2e", "e2e_pass")

# E2E failure
fc.connect("e2e_pass", "notify_e2e_fail", "Fail")

# E2E success
fc.connect("e2e_pass", "deploy_prod", "Pass")
fc.connect("deploy_prod", "notify_success")

fc.save("gallery_output/cicd_pipeline.excalidraw")
print("Created: gallery_output/cicd_pipeline.excalidraw")
