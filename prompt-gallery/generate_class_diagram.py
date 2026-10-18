#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a UML class diagram
d = Diagram()

# Title
d.text_box(200, 30, "Vehicle Class Hierarchy", font_size=24, color="black")

# Engine class (has-a relationship)
engine = d.box(100, 100, "Engine\n---\ntype: String\nhp: int\n---\nstart()\nstop()",
               width=180, height=120, color="teal")

# Vehicle base class
vehicle = d.box(400, 100, "Vehicle\n---\nmake: String\nmodel: String\nyear: int\n---\nstart()\nstop()",
                width=200, height=140, color="blue")

# Car subclass
car = d.box(300, 320, "Car\n---\nnumDoors: int\ntrunk_capacity: int",
            width=200, height=100, color="green")

# Motorcycle subclass
motorcycle = d.box(550, 320, "Motorcycle\n---\nhasSidecar: bool",
                   width=200, height=80, color="green")

# Relationships
# Inheritance (Car extends Vehicle)
d.arrow_between(car, vehicle, "extends", from_side="top", to_side="bottom")

# Inheritance (Motorcycle extends Vehicle)
d.arrow_between(motorcycle, vehicle, "extends", from_side="top", to_side="bottom")

# Composition (Vehicle has-a Engine)
d.arrow_between(engine, vehicle, "has-a", from_side="right", to_side="left")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/class_diagram.excalidraw"
d.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(d.elements)}")
