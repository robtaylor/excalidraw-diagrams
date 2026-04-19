#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a CI/CD pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Developer Pushes Code")

fc.process("trigger", "GitHub Triggers Workflow")
fc.process("tests", "Run Tests")
fc.decision("test_result", "Tests Pass?")

# Failure path
fc.position_at(150, 540)
fc.process("notify_fail", "Notify Developer")
fc.end("Stop")

# Success path
fc.position_at(450, 540)
fc.process("build", "Build Docker Image")
fc.process("push_registry", "Push to Registry")
fc.process("deploy_staging", "Deploy to Staging")
fc.process("e2e_tests", "Run E2E Tests")
fc.decision("e2e_result", "E2E Tests Pass?")

# E2E failure path
fc.position_at(350, 1100)
fc.process("notify_e2e_fail", "Notify Developer")

# E2E success path
fc.position_at(600, 1100)
fc.process("deploy_prod", "Deploy to Production")
fc.process("notify_success", "Send Success Notification")

# Connections
fc.connect("__start__", "trigger")
fc.connect("trigger", "tests")
fc.connect("tests", "test_result")
fc.connect("test_result", "notify_fail", "Fail")
fc.connect("notify_fail", "__end__")
fc.connect("test_result", "build", "Pass")
fc.connect("build", "push_registry")
fc.connect("push_registry", "deploy_staging")
fc.connect("deploy_staging", "e2e_tests")
fc.connect("e2e_tests", "e2e_result")
fc.connect("e2e_result", "notify_e2e_fail", "Fail")
fc.connect("e2e_result", "deploy_prod", "Pass")
fc.connect("deploy_prod", "notify_success")

fc.save("gallery_output/cicd_pipeline.excalidraw")
print("Created: gallery_output/cicd_pipeline.excalidraw")
