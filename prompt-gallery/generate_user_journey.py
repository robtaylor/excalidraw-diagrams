#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Flowchart

# Create user registration flow
fc = Flowchart(direction="vertical", spacing=100)

fc.start("Start Registration")
fc.process("enter_email", "Enter Email")
fc.decision("validate_fmt", "Valid Email Format?")

# Invalid format - show error and loop back
fc.position_at(100, 440)
fc.process("fmt_error", "Show Format Error")

# Valid format - continue
fc.position_at(400, 440)
fc.decision("check_exists", "Email Exists?")

# Email exists - prompt login
fc.position_at(200, 640)
fc.process("prompt_login", "Prompt Login")

# New email - continue registration
fc.position_at(500, 640)
fc.process("enter_pass", "Enter Password")
fc.decision("validate_strength", "Strong Password?")

# Weak password
fc.position_at(350, 940)
fc.process("pass_error", "Show Strength Error")

# Strong password - continue
fc.position_at(650, 940)
fc.process("create_acct", "Create Account")
fc.process("send_email", "Send Verification Email")
fc.process("click_link", "User Clicks Link")
fc.process("verified", "Account Verified")
fc.process("onboard", "Onboarding Tutorial")
fc.end("Registration Complete")

# Connections
fc.connect("__start__", "enter_email")
fc.connect("enter_email", "validate_fmt")
fc.connect("validate_fmt", "fmt_error", "Invalid")
fc.connect("fmt_error", "enter_email")  # Loop back
fc.connect("validate_fmt", "check_exists", "Valid")
fc.connect("check_exists", "prompt_login", "Yes")
fc.connect("check_exists", "enter_pass", "No")
fc.connect("enter_pass", "validate_strength")
fc.connect("validate_strength", "pass_error", "Weak")
fc.connect("pass_error", "enter_pass")  # Loop back
fc.connect("validate_strength", "create_acct", "Strong")
fc.connect("create_acct", "send_email")
fc.connect("send_email", "click_link")
fc.connect("click_link", "verified")
fc.connect("verified", "onboard")
fc.connect("onboard", "__end__")

fc.save("gallery_output/user_journey.excalidraw")
print("Created: gallery_output/user_journey.excalidraw")
