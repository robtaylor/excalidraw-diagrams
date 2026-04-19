#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create a user registration flowchart
fc = Flowchart(direction="vertical", spacing=90)

fc.start("Start")
fc.process("enter_email", "Enter Email")
fc.decision("validate_format", "Valid Email Format?")

# Invalid format path (loop back)
fc.position_at(150, 360)
fc.process("show_error", "Show Error")

# Valid format - continue
fc.position_at(450, 360)
fc.decision("check_exists", "Email Exists?")

# Email exists path
fc.position_at(250, 510)
fc.process("prompt_login", "Prompt Login")

# New email - continue
fc.position_at(550, 510)
fc.process("enter_password", "Enter Password")
fc.process("validate_password", "Validate Password Strength")
fc.process("create_account", "Create Account")
fc.process("send_email", "Send Verification Email")
fc.process("click_link", "User Clicks Link")
fc.process("verified", "Account Verified")
fc.process("onboarding", "Onboarding Tutorial")
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

fc.save("gallery_output/user_journey.excalidraw")
print("Created: gallery_output/user_journey.excalidraw")
