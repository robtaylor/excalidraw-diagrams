#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create CI/CD pipeline flowchart
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Developer Pushes Code")
fc.process("trigger", "GitHub Triggers Workflow")
fc.decision("tests", "Run Tests: Pass?")

# Fail path - left branch
fc.position_at(100, 440)
fc.process("notify_fail", "Notify Developer")
fc.end("Stop")

# Pass path - right branch continues down
fc.position_at(400, 440)
fc.process("build", "Build Docker Image")
fc.process("push", "Push to Registry")
fc.process("deploy_stg", "Deploy to Staging")
fc.decision("e2e", "Run E2E Tests: Pass?")

# E2E fail - loop back
fc.position_at(250, 940)
fc.process("notify_e2e", "Notify Developer")

# E2E pass - continue
fc.position_at(550, 940)
fc.process("deploy_prod", "Deploy to Production")
fc.process("success", "Send Success Notification")

# Connections
fc.connect("__start__", "trigger")
fc.connect("trigger", "tests")
fc.connect("tests", "notify_fail", "Fail")
fc.connect("notify_fail", "__end__")
fc.connect("tests", "build", "Pass")
fc.connect("build", "push")
fc.connect("push", "deploy_stg")
fc.connect("deploy_stg", "e2e")
fc.connect("e2e", "notify_e2e", "Fail")
fc.connect("e2e", "deploy_prod", "Pass")
fc.connect("deploy_prod", "success")

fc.save("gallery_output/cicd_pipeline.excalidraw")
print("Created: gallery_output/cicd_pipeline.excalidraw")
