#!/usr/bin/env python3
"""
Generate diagrams and run line routing validator to identify issues.
This helps identify systematic errors in the layout algorithm.
"""

import json
import os
import sys
import tempfile
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "tests"))

from excalidraw_generator import (
    Diagram,
    Flowchart,
    ArchitectureDiagram,
    AutoLayoutFlowchart,
    DiagramStyle,
    FlowchartStyle,
    LayoutConfig,
    ArchitectureStyle,
)
from line_routing_validator import LineRoutingValidator, Severity


def generate_cicd_pipeline():
    """CI/CD Pipeline flowchart - matches prompt gallery"""
    fc = AutoLayoutFlowchart(
        vertical_spacing=80,
        horizontal_spacing=100,
    )

    fc.add_node("start", "Developer\npushes code", shape="ellipse", color="green", node_type="terminal")
    fc.add_node("trigger", "GitHub triggers\nworkflow", color="blue", node_type="process")
    fc.add_node("tests", "Run Tests", color="blue", node_type="process")
    fc.add_node("test_decision", "Pass?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("notify_fail", "Notify developer", color="red", node_type="process")
    fc.add_node("build", "Build Docker\nImage", color="blue", node_type="process")
    fc.add_node("push", "Push to\nRegistry", color="blue", node_type="process")
    fc.add_node("staging", "Deploy to\nStaging", color="blue", node_type="process")
    fc.add_node("e2e", "Run E2E\nTests", color="blue", node_type="process")
    fc.add_node("e2e_decision", "Pass?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("production", "Deploy to\nProduction", color="green", node_type="process")
    fc.add_node("success", "Send success\nnotification", shape="ellipse", color="green", node_type="terminal")

    fc.add_edge("start", "trigger")
    fc.add_edge("trigger", "tests")
    fc.add_edge("tests", "test_decision")
    fc.add_edge("test_decision", "notify_fail", label="No")
    fc.add_edge("test_decision", "build", label="Yes")
    fc.add_edge("build", "push")
    fc.add_edge("push", "staging")
    fc.add_edge("staging", "e2e")
    fc.add_edge("e2e", "e2e_decision")
    fc.add_edge("e2e_decision", "notify_fail", label="No")
    fc.add_edge("e2e_decision", "production", label="Yes")
    fc.add_edge("production", "success")

    fc.compute_layout(two_column=True)
    return fc, "cicd_pipeline"


def generate_microservices():
    """Microservices architecture diagram - matches prompt gallery"""
    arch = ArchitectureDiagram()

    # User
    arch.user("user", "User", x=50, y=200)

    # Frontend
    arch.component("web", "Web\nFrontend", x=180, y=200, color="blue")

    # API Gateway
    arch.component("gateway", "API\nGateway", x=320, y=200, color="violet")

    # Services row
    arch.service("auth", "Auth\nService", x=200, y=350, color="blue")
    arch.service("product", "Product\nService", x=320, y=350, color="blue")
    arch.service("order", "Order\nService", x=440, y=350, color="blue")
    arch.service("payment", "Payment\nService", x=560, y=350, color="blue")

    # Databases
    arch.database("postgres", "PostgreSQL", x=280, y=500, color="green")
    arch.database("redis", "Redis", x=440, y=500, color="orange")

    # Connections
    arch.connect("user", "web", "HTTPS")
    arch.connect("web", "gateway", "REST")
    arch.connect("gateway", "auth", "gRPC")
    arch.connect("gateway", "product", "REST")
    arch.connect("gateway", "order", "REST")
    arch.connect("gateway", "payment", "gRPC")
    arch.connect("product", "postgres")
    arch.connect("order", "postgres")
    arch.connect("auth", "redis")
    arch.connect("payment", "redis")

    return arch, "microservices"


def generate_user_journey():
    """User registration flow - matches prompt gallery"""
    fc = AutoLayoutFlowchart(
        vertical_spacing=70,
        horizontal_spacing=100,
    )

    fc.add_node("start", "Start", shape="ellipse", color="green", node_type="terminal")
    fc.add_node("enter_email", "Enter Email", color="blue", node_type="process")
    fc.add_node("validate_email", "Valid\nFormat?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("show_error1", "Show Error", color="red", node_type="process")
    fc.add_node("check_exists", "Email\nExists?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("prompt_login", "Prompt\nLogin", color="orange", node_type="process")
    fc.add_node("enter_pass", "Enter\nPassword", color="blue", node_type="process")
    fc.add_node("validate_pass", "Strong\nPassword?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("create_account", "Create\nAccount", color="green", node_type="process")
    fc.add_node("send_email", "Send\nVerification", color="blue", node_type="process")
    fc.add_node("click_link", "User Clicks\nLink", color="blue", node_type="process")
    fc.add_node("verified", "Account\nVerified", color="green", node_type="process")
    fc.add_node("onboard", "Onboarding\nTutorial", color="blue", node_type="process")
    fc.add_node("end", "End", shape="ellipse", color="green", node_type="terminal")

    fc.add_edge("start", "enter_email")
    fc.add_edge("enter_email", "validate_email")
    fc.add_edge("validate_email", "show_error1", label="No")
    fc.add_edge("show_error1", "enter_email")
    fc.add_edge("validate_email", "check_exists", label="Yes")
    fc.add_edge("check_exists", "prompt_login", label="Yes")
    fc.add_edge("check_exists", "enter_pass", label="No")
    fc.add_edge("enter_pass", "validate_pass")
    fc.add_edge("validate_pass", "enter_pass", label="No")
    fc.add_edge("validate_pass", "create_account", label="Yes")
    fc.add_edge("create_account", "send_email")
    fc.add_edge("send_email", "click_link")
    fc.add_edge("click_link", "verified")
    fc.add_edge("verified", "onboard")
    fc.add_edge("onboard", "end")

    fc.compute_layout(two_column=True)
    return fc, "user_journey"


def generate_state_machine():
    """Order state machine - matches prompt gallery"""
    d = Diagram(diagram_style=DiagramStyle(roughness=0))

    # States in horizontal layout
    x_start = 50
    y_main = 150
    spacing = 150

    created = d.box(x_start, y_main, "Created", color="blue")
    pending = d.box(x_start + spacing, y_main, "Pending\nPayment", color="yellow")
    paid = d.box(x_start + 2*spacing, y_main, "Paid", color="green")
    processing = d.box(x_start + 3*spacing, y_main, "Processing", color="blue")
    shipped = d.box(x_start + 4*spacing, y_main, "Shipped", color="blue")
    delivered = d.box(x_start + 5*spacing, y_main, "Delivered", color="green")

    # Alternative states
    cancelled = d.box(x_start + 2*spacing, y_main + 120, "Cancelled", color="red")
    refunded = d.box(x_start + 4*spacing, y_main + 120, "Refunded", color="orange")

    # Transitions
    d.arrow_between(created, pending, label="checkout")
    d.arrow_between(pending, paid, label="payment_received")
    d.arrow_between(paid, processing, label="items_packed")
    d.arrow_between(processing, shipped, label="shipped")
    d.arrow_between(shipped, delivered, label="delivered")

    d.arrow_between(pending, cancelled, label="cancel")
    d.arrow_between(processing, cancelled, label="cancel")
    d.arrow_between(delivered, refunded, label="refund_approved")

    return d, "state_machine"


def generate_decision_tree():
    """Support ticket routing - matches prompt gallery"""
    fc = AutoLayoutFlowchart(
        vertical_spacing=80,
        horizontal_spacing=120,
    )

    fc.add_node("ticket", "New\nTicket", shape="ellipse", color="green", node_type="terminal")
    fc.add_node("urgent", "Urgent?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("priority", "Priority\nQueue", color="red", node_type="process")
    fc.add_node("billing", "Billing\nRelated?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("billing_team", "Billing\nTeam", color="blue", node_type="process")
    fc.add_node("technical", "Technical?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("complexity", "Simple\nIssue?", shape="diamond", color="yellow", node_type="decision")
    fc.add_node("tier1", "Tier 1\nSupport", color="blue", node_type="process")
    fc.add_node("tier2", "Tier 2\nSupport", color="violet", node_type="process")
    fc.add_node("general", "General\nSupport", color="gray", node_type="process")

    fc.add_edge("ticket", "urgent")
    fc.add_edge("urgent", "priority", label="Yes")
    fc.add_edge("urgent", "billing", label="No")
    fc.add_edge("billing", "billing_team", label="Yes")
    fc.add_edge("billing", "technical", label="No")
    fc.add_edge("technical", "complexity", label="Yes")
    fc.add_edge("technical", "general", label="No")
    fc.add_edge("complexity", "tier1", label="Yes")
    fc.add_edge("complexity", "tier2", label="No")

    fc.compute_layout()
    return fc, "decision_tree"


def generate_event_driven():
    """Event-driven architecture - matches prompt gallery"""
    arch = ArchitectureDiagram()

    # Order Service
    arch.service("order", "Order\nService", x=100, y=50, color="blue")

    # Event Bus (wider)
    arch.component("bus", "Event Bus\n(Kafka/SNS)", x=100, y=180, color="orange")

    # Consumer services
    arch.service("inventory", "Inventory\nService", x=0, y=320, color="green")
    arch.service("notification", "Notification\nService", x=150, y=320, color="violet")
    arch.service("analytics", "Analytics\nService", x=300, y=320, color="cyan")
    arch.service("shipping", "Shipping\nService", x=450, y=320, color="blue")

    # Event
    arch.connect("order", "bus", "OrderCreated")
    arch.connect("bus", "inventory", "subscribe")
    arch.connect("bus", "notification", "subscribe")
    arch.connect("bus", "analytics", "subscribe")
    arch.connect("bus", "shipping", "subscribe")

    return arch, "event_driven"


def generate_data_flow():
    """Data pipeline - matches prompt gallery"""
    d = Diagram()

    # Data sources
    y_source = 50
    d.box(50, y_source, "API", color="blue", width=80)
    d.box(150, y_source, "Database", shape="ellipse", color="green", width=90)
    d.box(260, y_source, "S3", color="orange", width=80)

    # Ingestion
    kafka = d.box(150, 150, "Kafka\n(Ingestion)", color="orange", width=120)

    # Processing
    transform = d.box(50, 280, "Transform", color="blue", width=100)
    validate = d.box(180, 280, "Validate", color="blue", width=100)
    enrich = d.box(310, 280, "Enrich", color="blue", width=100)

    spark = d.box(180, 350, "Spark Jobs", color="violet", width=120)

    # Data Warehouse
    snowflake = d.box(180, 450, "Snowflake\n(Warehouse)", shape="ellipse", color="cyan", width=140)

    # Analytics
    y_analytics = 550
    d.box(50, y_analytics, "Dashboards", color="green", width=100)
    d.box(180, y_analytics, "Reports", color="green", width=100)
    d.box(310, y_analytics, "ML Models", color="violet", width=100)

    return d, "data_flow"


def generate_network_topology():
    """Network architecture - matches prompt gallery

    Uses a hierarchical layout that avoids arrows crossing through elements.
    """
    d = Diagram()

    # Internet at top
    internet = d.box(300, 30, "Internet", shape="ellipse", color="gray")

    # Load Balancer below Internet
    lb = d.box(300, 120, "Load\nBalancer", color="violet")

    # Web Servers (main path continues straight down)
    web = d.box(300, 240, "Web\nServers", color="blue", width=100)

    # App Servers below Web
    app = d.box(300, 360, "App\nServers", color="blue", width=100)

    # Database layer at bottom
    primary = d.box(220, 480, "Primary\nDB", shape="ellipse", color="green", width=100)
    replica = d.box(400, 480, "Read\nReplica", shape="ellipse", color="green", width=100)

    # NAT Gateway and Bastion on the sides
    nat = d.box(80, 240, "NAT\nGateway", color="blue", width=100)
    bastion = d.box(500, 240, "Bastion\nHost", color="blue", width=100)

    # VPC boundary (draw first for background)
    # d.box(50, 180, "VPC", color="gray", width=550, height=400)

    # Main flow connections (vertical path)
    d.arrow_between(internet, lb)
    d.arrow_between(lb, web)
    d.arrow_between(web, app)
    d.arrow_between(app, primary)
    d.arrow_between(primary, replica, label="replication")

    return d, "network_topology"


def generate_class_diagram():
    """Class hierarchy - matches prompt gallery"""
    d = Diagram(diagram_style=DiagramStyle(roughness=0))

    # Base class
    vehicle = d.box(250, 50, "Vehicle\n─────────\n+ make: string\n+ model: string\n+ year: int\n─────────\n+ start()\n+ stop()",
                   color="blue", width=150, height=120)

    # Engine (composition)
    engine = d.box(480, 70, "Engine\n─────────\n+ horsepower: int\n+ type: string",
                  color="green", width=140, height=80)

    # Subclasses
    car = d.box(150, 250, "Car\n─────────\n+ numDoors: int\n+ trunk_capacity: float",
               color="blue", width=150, height=80)
    motorcycle = d.box(350, 250, "Motorcycle\n─────────\n+ hasSidecar: bool",
                      color="blue", width=150, height=80)

    # Relationships
    d.arrow_between(car, vehicle, from_side="top", to_side="bottom")
    d.arrow_between(motorcycle, vehicle, from_side="top", to_side="bottom")
    d.arrow_between(vehicle, engine, label="has-a")

    return d, "class_diagram"


def generate_deployment():
    """Kubernetes deployment - matches prompt gallery"""
    d = Diagram()

    # External
    registry = d.box(50, 50, "Container\nRegistry", color="gray", width=100)
    monitoring = d.box(550, 50, "Prometheus\nGrafana", color="violet", width=100)

    # Cluster boundary
    d.box(100, 120, "Kubernetes Cluster", color="blue", width=450, height=350)

    # Ingress
    ingress = d.box(300, 150, "Ingress\nController", color="orange", width=100)

    # Service
    service = d.box(300, 230, "Service\n(ClusterIP)", color="blue", width=100)

    # Deployment
    d.box(180, 300, "Deployment", color="green", width=280, height=130)

    # Pods
    pod1 = d.box(200, 340, "Pod\n[App+Sidecar]", color="cyan", width=80, height=60)
    pod2 = d.box(300, 340, "Pod\n[App+Sidecar]", color="cyan", width=80, height=60)
    pod3 = d.box(400, 340, "Pod\n[App+Sidecar]", color="cyan", width=80, height=60)

    # Config
    configmap = d.box(120, 400, "ConfigMap", color="yellow", width=80)
    secret = d.box(500, 400, "Secret", color="red", width=80)
    pvc = d.box(310, 470, "PVC", color="green", width=80)

    # Connections
    d.arrow_between(ingress, service)
    d.arrow_between(service, pod1)
    d.arrow_between(service, pod2)
    d.arrow_between(service, pod3)

    return d, "deployment"


def generate_all_diagrams():
    """Generate all diagrams and return as list of (diagram, name) tuples."""
    generators = [
        generate_cicd_pipeline,
        generate_microservices,
        generate_user_journey,
        generate_state_machine,
        generate_decision_tree,
        generate_event_driven,
        generate_data_flow,
        generate_network_topology,
        generate_class_diagram,
        generate_deployment,
    ]

    diagrams = []
    for gen in generators:
        try:
            diagram, name = gen()
            diagrams.append((diagram, name))
        except Exception as e:
            print(f"Error generating {gen.__name__}: {e}")

    return diagrams


def validate_diagrams(output_dir=None):
    """Generate diagrams, save them, and run validation."""
    if output_dir is None:
        output_dir = tempfile.mkdtemp(prefix="excalidraw_test_")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    diagrams = generate_all_diagrams()

    total_errors = 0
    total_warnings = 0
    total_info = 0
    all_issues = []

    print(f"\nValidating {len(diagrams)} diagrams...\n")
    print("=" * 70)

    for diagram, name in diagrams:
        filepath = output_path / f"{name}.excalidraw"
        diagram.save(filepath)

        validator = LineRoutingValidator(diagram_path=str(filepath))
        issues = validator.validate()
        summary = validator.get_summary()

        errors = summary['errors']
        warnings = summary['warnings']
        info = summary['info']

        total_errors += errors
        total_warnings += warnings
        total_info += info

        status = "✓" if errors == 0 else "✗"
        print(f"{status} {name}: {errors} errors, {warnings} warnings, {info} info")

        if issues:
            all_issues.append((name, issues))
            for issue in issues:
                print(f"    [{issue.severity.value.upper()}] {issue.issue_type}: {issue.message}")

    print("=" * 70)
    print(f"\nTOTAL: {total_errors} errors, {total_warnings} warnings, {total_info} info")
    print(f"Diagrams saved to: {output_dir}")

    # Group issues by type for analysis
    print("\n" + "=" * 70)
    print("ISSUE BREAKDOWN BY TYPE:")
    print("=" * 70)

    issue_by_type = {}
    for name, issues in all_issues:
        for issue in issues:
            key = issue.issue_type
            if key not in issue_by_type:
                issue_by_type[key] = []
            issue_by_type[key].append((name, issue))

    for issue_type, items in sorted(issue_by_type.items()):
        print(f"\n{issue_type} ({len(items)} occurrences):")
        for name, issue in items[:5]:  # Show first 5 examples
            details = issue.details or {}
            print(f"  - [{name}] {issue.message}")
            if details:
                print(f"    Details: {details}")

    return all_issues, output_path


if __name__ == "__main__":
    output_dir = sys.argv[1] if len(sys.argv) > 1 else None
    all_issues, output_path = validate_diagrams(output_dir)

    # Return exit code based on errors
    has_errors = any(issue.severity == Severity.ERROR for name, issues in all_issues for issue in issues)
    sys.exit(1 if has_errors else 0)
