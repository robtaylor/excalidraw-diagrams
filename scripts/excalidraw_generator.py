#!/usr/bin/env python3
"""
Excalidraw Diagram Generator

A Python library for programmatically generating Excalidraw diagrams.
Outputs .excalidraw JSON files that can be opened in Excalidraw.

Usage:
    from excalidraw_generator import Diagram, Box, Arrow, Text

    d = Diagram()
    box1 = d.box(100, 100, "Start", color="blue")
    box2 = d.box(300, 100, "End", color="green")
    d.arrow(box1, box2, "flow")
    d.save("my_diagram.excalidraw")
"""

import json
import random
import math
import uuid
from dataclasses import dataclass, field
from typing import Optional, Literal, Any
from pathlib import Path


# ============================================================================
# Constants (from Excalidraw source)
# ============================================================================

FONT_FAMILY = {
    "hand": 1,       # Virgil - hand-drawn style
    "normal": 2,     # Helvetica - clean
    "code": 3,       # Cascadia - monospace
    "excalifont": 5,
}

TEXT_ALIGN = {"left": "left", "center": "center", "right": "right"}
VERTICAL_ALIGN = {"top": "top", "middle": "middle", "bottom": "bottom"}

FILL_STYLE = {
    "hachure": "hachure",      # diagonal lines
    "solid": "solid",          # solid fill
    "cross-hatch": "cross-hatch",
    "zigzag": "zigzag",
}

STROKE_STYLE = {"solid": "solid", "dashed": "dashed", "dotted": "dotted"}

ROUNDNESS = {
    "sharp": None,
    "round": {"type": 3},  # Adaptive radius
}

ARROWHEADS = {
    "arrow": "arrow",
    "triangle": "triangle",
    "bar": "bar",
    "dot": "circle",  # 'dot' is legacy
    "circle": "circle",
    "diamond": "diamond",
    "none": None,
}

# Color palette (Excalidraw's open-color based palette)
COLORS = {
    "black": "#1e1e1e",
    "white": "#ffffff",
    "transparent": "transparent",
    # Stroke colors (shade index 4)
    "red": "#e03131",
    "pink": "#c2255c",
    "grape": "#9c36b5",
    "violet": "#6741d9",
    "blue": "#1971c2",
    "cyan": "#0c8599",
    "teal": "#099268",
    "green": "#2f9e44",
    "yellow": "#f08c00",
    "orange": "#e8590c",
    "gray": "#868e96",
    # Background colors (shade index 1) - lighter versions
    "red_bg": "#ffe3e3",
    "pink_bg": "#ffdeeb",
    "grape_bg": "#f3d9fa",
    "violet_bg": "#e5dbff",
    "blue_bg": "#d0ebff",
    "cyan_bg": "#c5f6fa",
    "teal_bg": "#c3fae8",
    "green_bg": "#d3f9d8",
    "yellow_bg": "#fff3bf",
    "orange_bg": "#ffe8cc",
    "gray_bg": "#e9ecef",
}

# Background color mapping for stroke colors
BG_FOR_STROKE = {
    "red": "red_bg",
    "pink": "pink_bg",
    "grape": "grape_bg",
    "violet": "violet_bg",
    "blue": "blue_bg",
    "cyan": "cyan_bg",
    "teal": "teal_bg",
    "green": "green_bg",
    "yellow": "yellow_bg",
    "orange": "orange_bg",
    "gray": "gray_bg",
    "black": "transparent",
}


# ============================================================================
# Element Classes
# ============================================================================

def _gen_id() -> str:
    """Generate a unique element ID."""
    return str(uuid.uuid4())[:20].replace("-", "")

def _gen_seed() -> int:
    """Generate a random seed for roughjs rendering."""
    return random.randint(1, 2_000_000_000)

def _base_element(
    elem_type: str,
    x: float,
    y: float,
    width: float,
    height: float,
    stroke_color: str = "#1e1e1e",
    bg_color: str = "transparent",
    fill_style: str = "solid",
    stroke_width: int = 2,
    stroke_style: str = "solid",
    roughness: int = 1,
    opacity: int = 100,
    angle: float = 0,
    roundness: Optional[dict] = None,
) -> dict:
    """Create a base element with common properties."""
    return {
        "id": _gen_id(),
        "type": elem_type,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": angle,
        "strokeColor": stroke_color,
        "backgroundColor": bg_color,
        "fillStyle": fill_style,
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": roughness,
        "opacity": opacity,
        "seed": _gen_seed(),
        "version": 1,
        "versionNonce": _gen_seed(),
        "index": None,
        "isDeleted": False,
        "groupIds": [],
        "frameId": None,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False,
        "roundness": roundness,
    }


def rectangle(
    x: float,
    y: float,
    width: float,
    height: float,
    color: str = "black",
    fill: bool = True,
    rounded: bool = True,
    **kwargs
) -> dict:
    """Create a rectangle element."""
    stroke = COLORS.get(color, color)
    bg = COLORS.get(BG_FOR_STROKE.get(color, "transparent"), "transparent") if fill else "transparent"

    elem = _base_element(
        "rectangle", x, y, width, height,
        stroke_color=stroke,
        bg_color=bg,
        roundness=ROUNDNESS["round"] if rounded else ROUNDNESS["sharp"],
        **kwargs
    )
    return elem


def ellipse(
    x: float,
    y: float,
    width: float,
    height: float,
    color: str = "black",
    fill: bool = True,
    **kwargs
) -> dict:
    """Create an ellipse element."""
    stroke = COLORS.get(color, color)
    bg = COLORS.get(BG_FOR_STROKE.get(color, "transparent"), "transparent") if fill else "transparent"

    elem = _base_element(
        "ellipse", x, y, width, height,
        stroke_color=stroke,
        bg_color=bg,
        **kwargs
    )
    return elem


def diamond(
    x: float,
    y: float,
    width: float,
    height: float,
    color: str = "black",
    fill: bool = True,
    **kwargs
) -> dict:
    """Create a diamond element."""
    stroke = COLORS.get(color, color)
    bg = COLORS.get(BG_FOR_STROKE.get(color, "transparent"), "transparent") if fill else "transparent"

    elem = _base_element(
        "diamond", x, y, width, height,
        stroke_color=stroke,
        bg_color=bg,
        **kwargs
    )
    return elem


def text(
    x: float,
    y: float,
    content: str,
    font_size: int = 20,
    font_family: str = "hand",
    color: str = "black",
    align: str = "center",
    **kwargs
) -> dict:
    """Create a text element."""
    stroke = COLORS.get(color, color)
    ff = FONT_FAMILY.get(font_family, 1)

    # Estimate dimensions based on content
    lines = content.split("\n")
    max_line_len = max(len(line) for line in lines)
    width = max_line_len * font_size * 0.6
    height = len(lines) * font_size * 1.35

    elem = _base_element(
        "text", x, y, width, height,
        stroke_color=stroke,
        bg_color="transparent",
        **kwargs
    )
    elem.update({
        "fontSize": font_size,
        "fontFamily": ff,
        "text": content,
        "textAlign": TEXT_ALIGN.get(align, "center"),
        "verticalAlign": "top",
        "containerId": None,
        "originalText": content,
        "autoResize": True,
        "lineHeight": 1.25,
    })
    return elem


def arrow(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    color: str = "black",
    start_head: Optional[str] = None,
    end_head: str = "arrow",
    label: Optional[str] = None,
    **kwargs
) -> list[dict]:
    """Create an arrow element, optionally with a label. Returns list of elements."""
    stroke = COLORS.get(color, color)

    # Calculate points relative to start
    dx = end_x - start_x
    dy = end_y - start_y

    elem = _base_element(
        "arrow", start_x, start_y,
        abs(dx), abs(dy),
        stroke_color=stroke,
        bg_color="transparent",
        **kwargs
    )
    elem.update({
        "points": [[0, 0], [dx, dy]],
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": ARROWHEADS.get(start_head),
        "endArrowhead": ARROWHEADS.get(end_head, "arrow"),
        "elbowed": False,
    })

    elements = [elem]

    # Add label if provided
    if label:
        mid_x = start_x + dx / 2
        mid_y = start_y + dy / 2 - 20  # offset above the line
        label_elem = text(mid_x, mid_y, label, font_size=16, color=color)
        elements.append(label_elem)

    return elements


def line(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    color: str = "black",
    **kwargs
) -> dict:
    """Create a line element."""
    stroke = COLORS.get(color, color)
    dx = end_x - start_x
    dy = end_y - start_y

    elem = _base_element(
        "line", start_x, start_y,
        abs(dx), abs(dy),
        stroke_color=stroke,
        bg_color="transparent",
        **kwargs
    )
    elem.update({
        "points": [[0, 0], [dx, dy]],
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": None,
    })
    return elem


# ============================================================================
# Diagram Class - High-Level API
# ============================================================================

@dataclass
class Element:
    """Wrapper for element with position tracking."""
    data: dict
    x: float
    y: float
    width: float
    height: float
    id: str = ""

    def __post_init__(self):
        self.id = self.data.get("id", "")

    @property
    def center_x(self) -> float:
        return self.x + self.width / 2

    @property
    def center_y(self) -> float:
        return self.y + self.height / 2

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    @property
    def top(self) -> float:
        return self.y

    @property
    def left(self) -> float:
        return self.x


class Diagram:
    """High-level API for creating Excalidraw diagrams."""

    def __init__(self, background: str = "#ffffff"):
        self.elements: list[dict] = []
        self.background = background

    def add(self, *elements: dict | list[dict]) -> None:
        """Add raw elements to the diagram."""
        for elem in elements:
            if isinstance(elem, list):
                self.elements.extend(elem)
            else:
                self.elements.append(elem)

    def box(
        self,
        x: float,
        y: float,
        label: str,
        width: float = 150,
        height: float = 60,
        color: str = "blue",
        shape: Literal["rectangle", "ellipse", "diamond"] = "rectangle",
        font_size: int = 18,
    ) -> Element:
        """Create a labeled box (rectangle, ellipse, or diamond)."""
        shape_funcs = {
            "rectangle": rectangle,
            "ellipse": ellipse,
            "diamond": diamond,
        }
        shape_elem = shape_funcs[shape](x, y, width, height, color=color)

        # Add centered text
        text_x = x + width / 2 - len(label) * font_size * 0.3
        text_y = y + height / 2 - font_size / 2
        text_elem = text(text_x, text_y, label, font_size=font_size, color=color)

        # Link text to shape
        shape_elem["boundElements"] = [{"id": text_elem["id"], "type": "text"}]
        text_elem["containerId"] = shape_elem["id"]
        text_elem["textAlign"] = "center"
        text_elem["verticalAlign"] = "middle"
        # Position text at shape center
        text_elem["x"] = x
        text_elem["y"] = y
        text_elem["width"] = width
        text_elem["height"] = height

        self.elements.extend([shape_elem, text_elem])
        return Element(shape_elem, x, y, width, height)

    def text_box(
        self,
        x: float,
        y: float,
        content: str,
        font_size: int = 20,
        color: str = "black",
    ) -> Element:
        """Create a standalone text element."""
        elem = text(x, y, content, font_size=font_size, color=color)
        self.elements.append(elem)
        return Element(elem, x, y, elem["width"], elem["height"])

    def arrow_between(
        self,
        source: Element,
        target: Element,
        label: Optional[str] = None,
        color: str = "black",
        from_side: Literal["right", "bottom", "left", "top", "auto"] = "auto",
        to_side: Literal["left", "top", "right", "bottom", "auto"] = "auto",
    ) -> None:
        """Draw an arrow between two elements."""
        # Determine connection points
        if from_side == "auto" and to_side == "auto":
            # Auto-detect best sides based on relative position
            dx = target.center_x - source.center_x
            dy = target.center_y - source.center_y

            if abs(dx) > abs(dy):
                # Horizontal connection
                from_side = "right" if dx > 0 else "left"
                to_side = "left" if dx > 0 else "right"
            else:
                # Vertical connection
                from_side = "bottom" if dy > 0 else "top"
                to_side = "top" if dy > 0 else "bottom"

        # Get start point
        if from_side == "right":
            sx, sy = source.right, source.center_y
        elif from_side == "left":
            sx, sy = source.left, source.center_y
        elif from_side == "bottom":
            sx, sy = source.center_x, source.bottom
        else:  # top
            sx, sy = source.center_x, source.top

        # Get end point
        if to_side == "left":
            ex, ey = target.left, target.center_y
        elif to_side == "right":
            ex, ey = target.right, target.center_y
        elif to_side == "top":
            ex, ey = target.center_x, target.top
        else:  # bottom
            ex, ey = target.center_x, target.bottom

        elems = arrow(sx, sy, ex, ey, color=color, label=label)
        self.elements.extend(elems)

    def line_between(
        self,
        source: Element,
        target: Element,
        color: str = "black",
    ) -> None:
        """Draw a line between two elements."""
        elem = line(
            source.center_x, source.center_y,
            target.center_x, target.center_y,
            color=color
        )
        self.elements.append(elem)

    def group(self, *elements: Element) -> str:
        """Group elements together. Returns group ID."""
        group_id = _gen_id()
        for elem in elements:
            if "groupIds" not in self.elements[self._find_element_index(elem.id)]:
                self.elements[self._find_element_index(elem.id)]["groupIds"] = []
            self.elements[self._find_element_index(elem.id)]["groupIds"].append(group_id)
        return group_id

    def _find_element_index(self, elem_id: str) -> int:
        for i, e in enumerate(self.elements):
            if e.get("id") == elem_id:
                return i
        return -1

    def to_dict(self) -> dict:
        """Export diagram as Excalidraw JSON dict."""
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "gridSize": 20,
                "gridStep": 5,
                "gridModeEnabled": False,
                "viewBackgroundColor": self.background,
            },
            "files": {},
        }

    def to_json(self, indent: int = 2) -> str:
        """Export diagram as JSON string."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def save(self, path: str | Path) -> Path:
        """Save diagram to file."""
        path = Path(path)
        if not path.suffix:
            path = path.with_suffix(".excalidraw")
        path.write_text(self.to_json())
        return path


# ============================================================================
# Flowchart Builder
# ============================================================================

class Flowchart(Diagram):
    """Specialized diagram for creating flowcharts."""

    def __init__(
        self,
        direction: Literal["horizontal", "vertical"] = "vertical",
        spacing: int = 80,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.direction = direction
        self.spacing = spacing
        self._nodes: dict[str, Element] = {}
        self._next_x = 100
        self._next_y = 100

    def node(
        self,
        node_id: str,
        label: str,
        shape: Literal["rectangle", "ellipse", "diamond"] = "rectangle",
        color: str = "blue",
        width: float = 150,
        height: float = 60,
    ) -> Element:
        """Add a node to the flowchart."""
        elem = self.box(
            self._next_x, self._next_y,
            label, width, height, color, shape
        )
        self._nodes[node_id] = elem

        # Update position for next node
        if self.direction == "vertical":
            self._next_y += height + self.spacing
        else:
            self._next_x += width + self.spacing

        return elem

    def start(self, label: str = "Start") -> Element:
        """Add a start node (rounded rectangle)."""
        return self.node("__start__", label, shape="ellipse", color="green")

    def end(self, label: str = "End") -> Element:
        """Add an end node."""
        return self.node("__end__", label, shape="ellipse", color="red")

    def process(self, node_id: str, label: str, color: str = "blue") -> Element:
        """Add a process node (rectangle)."""
        return self.node(node_id, label, shape="rectangle", color=color)

    def decision(self, node_id: str, label: str, color: str = "yellow") -> Element:
        """Add a decision node (diamond)."""
        return self.node(node_id, label, shape="diamond", color=color, width=120, height=80)

    def connect(
        self,
        from_id: str,
        to_id: str,
        label: Optional[str] = None,
        color: str = "black",
    ) -> None:
        """Connect two nodes with an arrow."""
        source = self._nodes.get(from_id)
        target = self._nodes.get(to_id)
        if source and target:
            self.arrow_between(source, target, label=label, color=color)

    def position_at(self, x: float, y: float) -> "Flowchart":
        """Set position for next node."""
        self._next_x = x
        self._next_y = y
        return self


# ============================================================================
# Architecture Diagram Builder
# ============================================================================

class ArchitectureDiagram(Diagram):
    """Specialized diagram for system architecture."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._components: dict[str, Element] = {}

    def component(
        self,
        comp_id: str,
        label: str,
        x: float,
        y: float,
        width: float = 150,
        height: float = 80,
        color: str = "blue",
    ) -> Element:
        """Add a system component."""
        elem = self.box(x, y, label, width, height, color)
        self._components[comp_id] = elem
        return elem

    def database(
        self,
        db_id: str,
        label: str,
        x: float,
        y: float,
        color: str = "green",
    ) -> Element:
        """Add a database component (ellipse)."""
        elem = self.box(x, y, label, 120, 60, color, shape="ellipse")
        self._components[db_id] = elem
        return elem

    def service(
        self,
        svc_id: str,
        label: str,
        x: float,
        y: float,
        color: str = "violet",
    ) -> Element:
        """Add a service component."""
        elem = self.box(x, y, label, 140, 70, color)
        self._components[svc_id] = elem
        return elem

    def user(
        self,
        user_id: str,
        label: str = "User",
        x: float = 100,
        y: float = 100,
    ) -> Element:
        """Add a user/actor."""
        elem = self.box(x, y, label, 80, 80, "gray", shape="ellipse")
        self._components[user_id] = elem
        return elem

    def connect(
        self,
        from_id: str,
        to_id: str,
        label: Optional[str] = None,
        bidirectional: bool = False,
        color: str = "black",
    ) -> None:
        """Connect two components."""
        source = self._components.get(from_id)
        target = self._components.get(to_id)
        if source and target:
            self.arrow_between(source, target, label=label, color=color)
            if bidirectional:
                self.arrow_between(target, source, color=color)


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    """CLI entry point for testing."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: excalidraw_generator.py <output_file>")
        print("\nExample diagram will be created.")

        # Create example diagram
        d = Diagram()
        box1 = d.box(100, 100, "Frontend", color="blue")
        box2 = d.box(350, 100, "Backend", color="green")
        box3 = d.box(600, 100, "Database", color="orange")

        d.arrow_between(box1, box2, "REST API")
        d.arrow_between(box2, box3, "SQL")

        output = Path("example.excalidraw")
        d.save(output)
        print(f"Created: {output}")
        return

    output_path = sys.argv[1]

    # Read JSON from stdin if available
    if not sys.stdin.isatty():
        data = json.load(sys.stdin)
        d = Diagram()
        # Process simple node/edge format
        nodes = {}
        for node in data.get("nodes", []):
            elem = d.box(
                node.get("x", 100),
                node.get("y", 100),
                node.get("label", "Node"),
                color=node.get("color", "blue"),
                shape=node.get("shape", "rectangle"),
            )
            nodes[node.get("id", node.get("label"))] = elem

        for edge in data.get("edges", []):
            source = nodes.get(edge.get("from"))
            target = nodes.get(edge.get("to"))
            if source and target:
                d.arrow_between(source, target, label=edge.get("label"))

        d.save(output_path)
        print(f"Created: {output_path}")
    else:
        print("Provide JSON input via stdin")
        print('Example: echo \'{"nodes":[{"id":"a","label":"A","x":100,"y":100}]}\' | python excalidraw_generator.py out.excalidraw')


if __name__ == "__main__":
    main()
