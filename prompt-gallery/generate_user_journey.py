#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a user registration flowchart
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Start")
fc.process("email", "Enter Email")
fc.decision("valid_fmt", "Valid Format?")

# Invalid branch - loops back
fc.position_at(100, 440)
fc.process("error1", "Show Error")

# Continue main flow
fc.position_at(300, 440)
fc.decision("exists", "Email Exists?")

fc.position_at(100, 640)
fc.process("login", "Prompt Login")

fc.position_at(300, 640)
fc.process("password", "Enter Password")
fc.process("validate_pwd", "Validate Password Strength")
fc.process("create", "Create Account")
fc.process("send_email", "Send Verification Email")
fc.process("click", "User Clicks Link")
fc.process("verified", "Account Verified")
fc.process("tutorial", "Onboarding Tutorial")
fc.end("End")

# Connections
fc.connect("__start__", "email")
fc.connect("email", "valid_fmt")
fc.connect("valid_fmt", "error1", "Invalid")
fc.connect("error1", "email")  # Loop back
fc.connect("valid_fmt", "exists", "Valid")
fc.connect("exists", "login", "Yes")
fc.connect("exists", "password", "No")
fc.connect("password", "validate_pwd")
fc.connect("validate_pwd", "create")
fc.connect("create", "send_email")
fc.connect("send_email", "click")
fc.connect("click", "verified")
fc.connect("verified", "tutorial")
fc.connect("tutorial", "__end__")

fc.save("gallery_output/user_journey.excalidraw")
print("Created: user_journey.excalidraw")
