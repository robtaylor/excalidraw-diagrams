#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create UML class diagram
d = Diagram()

# Title
d.text_box(300, 30, "Vehicle Class Hierarchy", font_size=24)

# Engine class (composition)
engine = d.box(100, 120, "Engine\n\nstart()\nstop()", color="teal", width=140, height=100)

# Vehicle base class
vehicle = d.box(350, 120, "Vehicle\n\nmake: string\nmodel: string\nyear: int\n\nstart()\nstop()", color="blue", width=180, height=140)

# Car subclass
car = d.box(250, 340, "Car\n\nnumDoors: int\ntrunk_capacity: int", color="green", width=180, height=100)

# Motorcycle subclass
motorcycle = d.box(480, 340, "Motorcycle\n\nhasSidecar: bool", color="green", width=180, height=100)

# Inheritance arrows (from subclass to superclass)
d.arrow_between(car, vehicle, "", from_side="top", to_side="bottom")
d.arrow_between(motorcycle, vehicle, "", from_side="top", to_side="bottom")

# Composition arrow (Vehicle has-a Engine)
d.arrow_between(vehicle, engine, "has-a", from_side="left", to_side="right")

# Add labels
d.text_box(260, 290, "extends", font_size=14, color="gray")
d.text_box(490, 290, "extends", font_size=14, color="gray")

d.save("gallery_output/class_diagram.excalidraw")
print("✓ Created: gallery_output/class_diagram.excalidraw")
