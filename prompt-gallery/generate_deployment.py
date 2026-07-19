#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a Kubernetes deployment architecture diagram
d = Diagram()

# Title
d.text_box(300, 30, "Kubernetes Deployment Architecture", font_size=24)

# External components
d.text_box(50, 90, "External", font_size=16, color="gray")
registry = d.box(80, 120, "Container\nRegistry", color="gray", width=130, height=70)
monitoring = d.box(80, 220, "Monitoring\n(Prometheus/Grafana)", color="gray", width=160, height=70)

# Kubernetes cluster boundary
d.text_box(300, 90, "Kubernetes Cluster", font_size=20, color="blue")

# Ingress
ingress = d.box(320, 140, "Ingress Controller", color="violet", width=160)

# Service
service = d.box(320, 260, "Service (ClusterIP)", color="cyan", width=160)

# Deployment
d.text_box(280, 350, "Deployment", font_size=14, color="blue")

# Pods
pod1 = d.box(250, 390, "Pod 1\nApp Container\nSidecar", color="blue", width=100, height=80)
pod2 = d.box(370, 390, "Pod 2\nApp Container\nSidecar", color="blue", width=100, height=80)
pod3 = d.box(490, 390, "Pod 3\nApp Container\nSidecar", color="blue", width=100, height=80)

# Config and Storage
configmap = d.box(620, 260, "ConfigMap", color="orange", width=120)
secret = d.box(620, 360, "Secret", color="red", width=120)
pvc = d.box(620, 460, "PersistentVolumeClaim", color="green", width=180, height=60)

# Connections
d.arrow_between(registry, pod1, "pull")
d.arrow_between(monitoring, pod1, "scrape")
d.arrow_between(ingress, service, "route")
d.arrow_between(service, pod1, "")
d.arrow_between(service, pod2, "")
d.arrow_between(service, pod3, "")
d.arrow_between(configmap, pod1, "mount")
d.arrow_between(secret, pod2, "mount")
d.arrow_between(pvc, pod3, "mount")

d.save("gallery_output/deployment.excalidraw")
print("Created: deployment.excalidraw")
