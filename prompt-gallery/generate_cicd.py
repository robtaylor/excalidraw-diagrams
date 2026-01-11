#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create CI/CD pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Developer pushes code")
fc.process("trigger", "GitHub triggers workflow")
fc.process("tests", "Run Tests")
fc.decision("test_result", "Tests Pass?")

# Fail branch
fc.position_at(100, 540)
fc.process("notify_fail", "Notify developer")
fc.end("Stop")

# Success branch continues
fc.position_at(400, 540)
fc.process("build", "Build Docker Image")
fc.process("push", "Push to Registry")
fc.process("deploy_staging", "Deploy to Staging")
fc.process("e2e", "Run E2E Tests")
fc.decision("e2e_result", "E2E Pass?")

# E2E fail - back to notify
fc.position_at(600, 1140)
fc.process("notify_e2e", "Notify developer")

# E2E success
fc.position_at(400, 1240)
fc.process("deploy_prod", "Deploy to Production")
fc.process("success_notify", "Send success notification")

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
fc.connect("e2e_result", "notify_e2e", "Fail")
fc.connect("e2e_result", "deploy_prod", "Pass")
fc.connect("deploy_prod", "success_notify")

fc.save("gallery_output/cicd_pipeline.excalidraw")
print("✓ Created: gallery_output/cicd_pipeline.excalidraw")
