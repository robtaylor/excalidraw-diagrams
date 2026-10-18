#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a user registration flowchart
fc = Flowchart(direction="vertical", spacing=90)

# Start
fc.start("Start")

# Enter email
fc.process("enter_email", "Enter Email")

# Validate email format
fc.decision("validate_format", "Valid Format?")

# Invalid format path
fc.position_at(100, 340)
fc.process("show_error", "Show Error")

# Valid format - check if exists
fc.position_at(400, 340)
fc.decision("check_exists", "Email Exists?")

# Email exists - prompt login
fc.position_at(200, 480)
fc.process("prompt_login", "Prompt Login")

# Email doesn't exist - continue
fc.position_at(550, 480)
fc.process("enter_password", "Enter Password")
fc.process("validate_password", "Validate Password\nStrength")
fc.process("create_account", "Create Account")
fc.process("send_email", "Send Verification\nEmail")
fc.process("click_link", "User Clicks\nLink")
fc.process("verified", "Account Verified")
fc.process("onboarding", "Onboarding\nTutorial")
fc.end("End")

# Connections
fc.connect("__start__", "enter_email")
fc.connect("enter_email", "validate_format")
fc.connect("validate_format", "show_error", "Invalid")
fc.connect("show_error", "enter_email")  # Loop back
fc.connect("validate_format", "check_exists", "Valid")
fc.connect("check_exists", "prompt_login", "Yes")
fc.connect("check_exists", "enter_password", "No")
fc.connect("enter_password", "validate_password")
fc.connect("validate_password", "create_account")
fc.connect("create_account", "send_email")
fc.connect("send_email", "click_link")
fc.connect("click_link", "verified")
fc.connect("verified", "onboarding")
fc.connect("onboarding", "__end__")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/user_journey.excalidraw"
fc.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(fc.elements)}")
