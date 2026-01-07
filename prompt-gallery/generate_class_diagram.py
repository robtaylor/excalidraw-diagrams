#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create UML class diagram
d = Diagram()

# Add title
d.text_box(200, 30, "Vehicle Class Hierarchy", font_size=24)

# Engine class (composition)
engine = d.box(50, 120, "Engine\n---\ntype: string\nhorsepower: int\n---\nstart()\nstop()",
               width=180, height=120, color="teal")

# Vehicle base class
vehicle = d.box(320, 120, "Vehicle\n---\nmake: string\nmodel: string\nyear: int\n---\nstart()\nstop()",
                width=200, height=140, color="blue")

# Car subclass
car = d.box(200, 340, "Car\n---\nnumDoors: int\ntrunk_capacity: int\n---\nopenTrunk()",
            width=200, height=120, color="green")

# Motorcycle subclass
motorcycle = d.box(460, 340, "Motorcycle\n---\nhasSidecar: bool\n---\nleanIntoTurn()",
                   width=200, height=100, color="green")

# Relationships
# Vehicle has-a Engine (composition)
d.arrow_between(vehicle, engine, "has-a", from_side="left", to_side="right")

# Inheritance arrows (from subclass to superclass)
d.arrow_between(car, vehicle, "extends", from_side="top", to_side="bottom")
d.arrow_between(motorcycle, vehicle, "extends", from_side="top", to_side="bottom")

d.save("gallery_output/class_diagram.excalidraw")
print("Created: gallery_output/class_diagram.excalidraw")
