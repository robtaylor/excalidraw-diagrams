#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a Kubernetes deployment architecture diagram
d = Diagram()

# Title
d.text_box(300, 30, "Kubernetes Deployment Architecture", font_size=24, color="black")

# Kubernetes Cluster boundary
d.text_box(50, 90, "Kubernetes Cluster", font_size=20, color="blue")

# Ingress Controller
ingress = d.box(100, 140, "Ingress\nController", width=160, height=70, color="blue")

# Service
service = d.box(100, 260, "Service\n(ClusterIP)", width=160, height=70, color="cyan")

# Deployment label
d.text_box(330, 140, "Deployment", font_size=18, color="green")

# Pods (3 replicas)
pod1 = d.box(320, 180, "Pod 1\nApp + Sidecar", width=140, height=80, color="green")
pod2 = d.box(480, 180, "Pod 2\nApp + Sidecar", width=140, height=80, color="green")
pod3 = d.box(640, 180, "Pod 3\nApp + Sidecar", width=140, height=80, color="green")

# ConfigMap and Secret
configmap = d.box(320, 320, "ConfigMap", width=140, height=60, color="orange")
secret = d.box(480, 320, "Secret", width=140, height=60, color="red")

# PersistentVolumeClaim
pvc = d.box(640, 320, "Persistent\nVolumeClaim", width=140, height=60, color="violet")

# External components
d.text_box(50, 440, "External", font_size=18, color="gray")
registry = d.box(100, 480, "Container\nRegistry", width=150, height=70, color="gray")
monitoring = d.box(280, 480, "Monitoring\n(Prometheus)", width=150, height=70, color="gray")

# Connections
d.arrow_between(ingress, service, "route")
d.arrow_between(service, pod1, "load balance")
d.arrow_between(service, pod2, "load balance")
d.arrow_between(service, pod3, "load balance")

# ConfigMap/Secret to Pods
d.arrow_between(configmap, pod1, "mount")
d.arrow_between(configmap, pod2, "mount")
d.arrow_between(secret, pod2, "mount")
d.arrow_between(pvc, pod3, "mount")

# External connections
d.arrow_between(registry, pod1, "pull image")
d.arrow_between(monitoring, pod2, "scrape")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/deployment.excalidraw"
d.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(d.elements)}")
