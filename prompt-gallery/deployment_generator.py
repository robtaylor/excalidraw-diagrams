#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a Kubernetes deployment architecture diagram
d = Diagram()

# Title
d.text_box(280, 20, "Kubernetes Cluster Architecture", font_size=28)

# External components
d.text_box(50, 80, "External", font_size=18, color="gray")
registry = d.box(50, 120, "Container\nRegistry", color="cyan", width=140)
monitoring = d.box(50, 240, "Monitoring\n(Prometheus)", color="cyan", width=140)

# Cluster boundary
d.text_box(260, 80, "Kubernetes Cluster", font_size=20, color="blue")

# Ingress
ingress = d.box(300, 130, "Ingress\nController", color="violet", width=140)

# Service
service = d.box(300, 240, "Service\n(ClusterIP)", color="orange", width=140)

# Deployment
d.text_box(480, 180, "Deployment", font_size=16, color="green")

# Pod replicas
pod1 = d.box(480, 220, "Pod 1\nApp + Sidecar", color="green", width=120, height=70)
pod2 = d.box(630, 220, "Pod 2\nApp + Sidecar", color="green", width=120, height=70)
pod3 = d.box(780, 220, "Pod 3\nApp + Sidecar", color="green", width=120, height=70)

# ConfigMap and Secret
configmap = d.box(480, 380, "ConfigMap", color="blue", width=120)
secret = d.box(630, 380, "Secret", color="red", width=120)

# Persistent Volume Claim
pvc = d.box(780, 380, "PersistentVolume\nClaim", color="orange", width=150, height=70)

# Connections
d.arrow_between(ingress, service, "routes to")
d.arrow_between(service, pod1)
d.arrow_between(service, pod2)
d.arrow_between(service, pod3)

# Config connections
d.arrow_between(configmap, pod1, from_side="top", to_side="bottom")
d.arrow_between(configmap, pod2, from_side="top", to_side="bottom")
d.arrow_between(secret, pod2, from_side="top", to_side="bottom")
d.arrow_between(pvc, pod3, from_side="top", to_side="bottom")

# External connections
d.arrow_between(registry, pod1, "pulls image", from_side="right", to_side="left")
d.arrow_between(monitoring, pod1, "scrapes", from_side="right", to_side="left")

d.save("gallery_output/deployment.excalidraw")
print("Created: gallery_output/deployment.excalidraw")
