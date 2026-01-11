#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create user registration flow
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Start")
fc.process("enter_email", "Enter Email")
fc.decision("valid_format", "Valid Email Format?")

# Invalid format - show error and loop back
fc.position_at(150, 440)
fc.process("show_error", "Show Error")

# Continue with valid email
fc.position_at(450, 440)
fc.decision("email_exists", "Email Exists?")

# Email exists - prompt login
fc.position_at(650, 580)
fc.process("prompt_login", "Prompt Login")

# New email - continue registration
fc.position_at(450, 680)
fc.process("enter_password", "Enter Password")
fc.process("validate_strength", "Validate Password Strength")
fc.process("create_account", "Create Account")
fc.process("send_verification", "Send Verification Email")
fc.process("click_link", "User Clicks Link")
fc.process("verified", "Account Verified")
fc.process("onboarding", "Onboarding Tutorial")
fc.end("End")

# Connections
fc.connect("__start__", "enter_email")
fc.connect("enter_email", "valid_format")
fc.connect("valid_format", "show_error", "Invalid")
fc.connect("show_error", "enter_email", "retry")
fc.connect("valid_format", "email_exists", "Valid")
fc.connect("email_exists", "prompt_login", "Yes")
fc.connect("email_exists", "enter_password", "No")
fc.connect("enter_password", "validate_strength")
fc.connect("validate_strength", "create_account")
fc.connect("create_account", "send_verification")
fc.connect("send_verification", "click_link")
fc.connect("click_link", "verified")
fc.connect("verified", "onboarding")
fc.connect("onboarding", "__end__")

fc.save("gallery_output/user_journey.excalidraw")
print("✓ Created: gallery_output/user_journey.excalidraw")
