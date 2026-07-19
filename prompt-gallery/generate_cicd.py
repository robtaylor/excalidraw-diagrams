#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a CI/CD pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Developer pushes code")
fc.process("trigger", "GitHub triggers workflow")
fc.process("tests", "Run Tests")
fc.decision("test_pass", "Pass?")

# Fail branch
fc.position_at(100, 540)
fc.process("notify_fail", "Notify developer")
fc.end("Stop")

# Pass branch
fc.position_at(300, 540)
fc.process("build", "Build Docker Image")
fc.process("push", "Push to Registry")
fc.process("deploy_stg", "Deploy to Staging")
fc.process("e2e", "Run E2E Tests")
fc.decision("e2e_pass", "Pass?")

fc.position_at(300, 1140)
fc.process("deploy_prod", "Deploy to Production")
fc.process("notify_success", "Send success notification")

# Connections
fc.connect("__start__", "trigger")
fc.connect("trigger", "tests")
fc.connect("tests", "test_pass")
fc.connect("test_pass", "notify_fail", "Fail")
fc.connect("notify_fail", "__end__")
fc.connect("test_pass", "build", "Pass")
fc.connect("build", "push")
fc.connect("push", "deploy_stg")
fc.connect("deploy_stg", "e2e")
fc.connect("e2e", "e2e_pass")
fc.connect("e2e_pass", "notify_fail", "Fail")
fc.connect("e2e_pass", "deploy_prod", "Pass")
fc.connect("deploy_prod", "notify_success")

fc.save("gallery_output/cicd_pipeline.excalidraw")
print("Created: cicd_pipeline.excalidraw")
