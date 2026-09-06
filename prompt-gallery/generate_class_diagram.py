#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# UML Class Diagram for Vehicle hierarchy
d = Diagram()

# Engine class (composition relationship)
engine = d.box(550, 80, "Engine\n-----------\n+ start()\n+ stop()", width=150, height=100, color="teal")

# Base Vehicle class
vehicle = d.box(300, 80, "Vehicle\n-----------\n+ make: string\n+ model: string\n+ year: int\n-----------\n+ start()\n+ stop()", width=180, height=150, color="blue")

# Car subclass
car = d.box(150, 320, "Car\n-----------\n+ numDoors: int\n+ trunk_capacity: float\n-----------\n(extends Vehicle)", width=180, height=120, color="green")

# Motorcycle subclass
motorcycle = d.box(450, 320, "Motorcycle\n-----------\n+ hasSidecar: bool\n-----------\n(extends Vehicle)", width=180, height=120, color="green")

# Inheritance arrows (from subclass to parent)
d.arrow_between(car, vehicle, label="extends", from_side="top", to_side="bottom")
d.arrow_between(motorcycle, vehicle, label="extends", from_side="top", to_side="bottom")

# Composition relationship (Vehicle has-a Engine)
d.arrow_between(vehicle, engine, label="has-a", from_side="right", to_side="left")

d.save("gallery_output/class_diagram.excalidraw")
print("Created: gallery_output/class_diagram.excalidraw")
