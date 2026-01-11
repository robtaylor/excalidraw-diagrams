#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create Kubernetes deployment architecture
d = Diagram()

# Title
d.text_box(380, 30, "Kubernetes Deployment Architecture", font_size=24)

# External services
d.text_box(100, 100, "External", font_size=18, color="black")
registry = d.box(80, 140, "Container\nRegistry", color="orange", width=130, height=80)
monitoring = d.box(80, 250, "Prometheus/\nGrafana", color="violet", width=130, height=80)

# Kubernetes Cluster boundary
d.text_box(280, 100, "Kubernetes Cluster", font_size=20, color="blue")

# Ingress
ingress = d.box(350, 160, "Ingress Controller", color="cyan", width=160, height=60)

# Service
service = d.box(360, 270, "Service\n(ClusterIP)", color="violet", width=140, height=70)

# Deployment
d.text_box(300, 380, "Deployment", font_size=16, color="green")

# Pods
pod1 = d.box(280, 420, "Pod 1\nApp + Sidecar", color="blue", width=120, height=80)
pod2 = d.box(430, 420, "Pod 2\nApp + Sidecar", color="blue", width=120, height=80)
pod3 = d.box(580, 420, "Pod 3\nApp + Sidecar", color="blue", width=120, height=80)

# ConfigMap and Secret
configmap = d.box(750, 280, "ConfigMap", color="teal", width=120, height=60)
secret = d.box(750, 370, "Secret", color="red", width=120, height=60)

# PersistentVolumeClaim
pvc = d.box(750, 460, "PersistentVolumeClaim", color="green", width=180, height=60)

# Connections
d.arrow_between(ingress, service, "")
d.arrow_between(service, pod1, "")
d.arrow_between(service, pod2, "")
d.arrow_between(service, pod3, "")
d.arrow_between(registry, pod1, "pull", from_side="right", to_side="left")
d.arrow_between(monitoring, pod1, "metrics", from_side="right", to_side="left")
d.arrow_between(configmap, pod1, "config")
d.arrow_between(configmap, pod2, "config")
d.arrow_between(configmap, pod3, "config")
d.arrow_between(secret, pod1, "secrets")
d.arrow_between(secret, pod2, "secrets")
d.arrow_between(secret, pod3, "secrets")
d.arrow_between(pvc, pod1, "storage")
d.arrow_between(pvc, pod2, "storage")
d.arrow_between(pvc, pod3, "storage")

d.save("gallery_output/deployment.excalidraw")
print("✓ Created: gallery_output/deployment.excalidraw")
