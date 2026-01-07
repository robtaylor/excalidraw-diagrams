#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create Kubernetes deployment architecture
d = Diagram()

# Add title
d.text_box(250, 30, "Kubernetes Deployment", font_size=24)

# External components
registry = d.box(50, 120, "Container\nRegistry", width=140, height=80, color="gray")
monitoring = d.box(650, 120, "Monitoring\nPrometheus\nGrafana", width=140, height=100, color="gray")

# Kubernetes Cluster boundary
d.text_box(100, 250, "Kubernetes Cluster", font_size=20, color="blue")

# Ingress Controller
ingress = d.box(320, 300, "Ingress\nController", width=150, height=80, color="violet")

# Service
service = d.box(320, 430, "Service\n(ClusterIP)", width=150, height=70, color="blue")

# Deployment with pods
d.text_box(250, 550, "Deployment", font_size=18, color="green")

# Three pod replicas
pod1 = d.box(100, 600, "Pod 1\nApp Container\nSidecar", width=140, height=100, color="green")
pod2 = d.box(280, 600, "Pod 2\nApp Container\nSidecar", width=140, height=100, color="green")
pod3 = d.box(460, 600, "Pod 3\nApp Container\nSidecar", width=140, height=100, color="green")

# ConfigMap and Secret
configmap = d.box(50, 770, "ConfigMap", width=120, height=60, color="orange")
secret = d.box(210, 770, "Secret", width=120, height=60, color="red")

# PersistentVolumeClaim
pvc = d.box(400, 770, "PersistentVolume\nClaim", width=160, height=70, color="teal")

# Connections
# Ingress to Service
d.arrow_between(ingress, service, "route")

# Service to Pods
d.arrow_between(service, pod1)
d.arrow_between(service, pod2)
d.arrow_between(service, pod3)

# ConfigMap and Secret to Pods
d.arrow_between(configmap, pod1, "config")
d.arrow_between(configmap, pod2, "config")
d.arrow_between(configmap, pod3, "config")

d.arrow_between(secret, pod1, "secrets")
d.arrow_between(secret, pod2, "secrets")
d.arrow_between(secret, pod3, "secrets")

# PVC to Pods
d.arrow_between(pvc, pod1, "volume")
d.arrow_between(pvc, pod2, "volume")
d.arrow_between(pvc, pod3, "volume")

# External connections
d.arrow_between(registry, pod1, "pull")
d.arrow_between(registry, pod2, "pull")
d.arrow_between(registry, pod3, "pull")

d.arrow_between(monitoring, pod1, "scrape")
d.arrow_between(monitoring, pod2, "scrape")
d.arrow_between(monitoring, pod3, "scrape")

d.save("gallery_output/deployment.excalidraw")
print("Created: gallery_output/deployment.excalidraw")
