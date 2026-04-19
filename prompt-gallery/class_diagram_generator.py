#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a UML class diagram
d = Diagram()

# Title
d.text_box(200, 20, "Vehicle Class Hierarchy", font_size=24)

# Vehicle base class
vehicle = d.box(250, 100, "Vehicle\n---\nmake: string\nmodel: string\nyear: int\n---\nstart()\nstop()",
                width=200, height=140, color="blue")

# Car subclass
car = d.box(100, 320, "Car\n---\nnumDoors: int\ntrunk_capacity: float\n---\ninherits Vehicle",
            width=200, height=120, color="green")

# Motorcycle subclass
motorcycle = d.box(400, 320, "Motorcycle\n---\nhasSidecar: bool\n---\ninherits Vehicle",
                   width=200, height=100, color="green")

# Engine class
engine = d.box(520, 100, "Engine\n---\nhorsepower: int\ncylinders: int\n---\nignite()\nshutdown()",
               width=180, height=120, color="orange")

# Inheritance arrows (from subclasses to base class)
d.arrow_between(car, vehicle, "extends", from_side="top", to_side="bottom")
d.arrow_between(motorcycle, vehicle, "extends", from_side="top", to_side="bottom")

# Composition arrow (Vehicle has-a Engine)
d.arrow_between(vehicle, engine, "has-a", from_side="right", to_side="left")

d.save("gallery_output/class_diagram.excalidraw")
print("Created: gallery_output/class_diagram.excalidraw")
