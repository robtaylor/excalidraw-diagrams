#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a UML class diagram
d = Diagram()

# Title
d.text_box(300, 30, "Vehicle Class Hierarchy", font_size=24)

# Vehicle base class
vehicle = d.box(300, 120, "Vehicle\n\nmake: string\nmodel: string\nyear: int\n\nstart()\nstop()",
                width=200, height=120, color="blue")

# Subclasses
car = d.box(150, 320, "Car\n\nnumDoors: int\ntrunk_capacity: int",
            width=180, height=80, color="green")
motorcycle = d.box(450, 320, "Motorcycle\n\nhasSidecar: bool",
                   width=180, height=60, color="green")

# Engine class (composition)
engine = d.box(600, 120, "Engine\n\nhorsepower: int\ntype: string\n\nstart()\nstop()",
               width=180, height=100, color="orange")

# Inheritance arrows (from child to parent)
d.arrow_between(car, vehicle, "extends")
d.arrow_between(motorcycle, vehicle, "extends")

# Composition (has-a relationship)
d.arrow_between(vehicle, engine, "has-a")

d.save("gallery_output/class_diagram.excalidraw")
print("Created: class_diagram.excalidraw")
