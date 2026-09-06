#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# User Registration Flow
fc = Flowchart(direction="vertical", spacing=90)

fc.start("Start")
fc.process("enter_email", "Enter Email")
fc.decision("email_valid", "Valid Format?")

# Invalid email path - loops back
fc.position_at(100, 380)
fc.process("show_error", "Show Error")

# Valid email continues
fc.position_at(400, 380)
fc.decision("email_exists", "Email Exists?")

# Email exists - prompt login
fc.position_at(250, 540)
fc.process("prompt_login", "Prompt Login")

# Email doesn't exist - continue registration
fc.position_at(550, 540)
fc.process("enter_password", "Enter Password")
fc.process("validate_strength", "Validate Password Strength")
fc.process("create_account", "Create Account")
fc.process("send_email", "Send Verification Email")
fc.process("click_link", "User Clicks Link")
fc.process("verified", "Account Verified")
fc.process("onboarding", "Onboarding Tutorial")
fc.end("End")

# Connections
fc.connect("__start__", "enter_email")
fc.connect("enter_email", "email_valid")

# Invalid email loop
fc.connect("email_valid", "show_error", "Invalid")
fc.connect("show_error", "enter_email")

# Valid email
fc.connect("email_valid", "email_exists", "Valid")

# Email exists branch
fc.connect("email_exists", "prompt_login", "Yes")

# Email doesn't exist branch
fc.connect("email_exists", "enter_password", "No")
fc.connect("enter_password", "validate_strength")
fc.connect("validate_strength", "create_account")
fc.connect("create_account", "send_email")
fc.connect("send_email", "click_link")
fc.connect("click_link", "verified")
fc.connect("verified", "onboarding")
fc.connect("onboarding", "__end__")

fc.save("gallery_output/user_journey.excalidraw")
print("Created: gallery_output/user_journey.excalidraw")
