#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Kubernetes Deployment Architecture
d = Diagram()

# External components
d.text_box(50, 30, "External", font_size=20, color="gray")
registry = d.box(80, 70, "Container\nRegistry", color="gray", width=140)
monitoring = d.box(80, 180, "Monitoring\n(Prometheus)", color="gray", width=140)

# Kubernetes Cluster boundary label
d.text_box(300, 30, "Kubernetes Cluster", font_size=22, color="blue")

# Ingress
ingress = d.box(350, 100, "Ingress Controller", color="orange", width=180)

# Service
service = d.box(360, 220, "Service (ClusterIP)", color="violet", width=160)

# Deployment
d.text_box(320, 330, "Deployment", font_size=18, color="blue")

# Pod replicas
pod1 = d.box(280, 380, "Pod 1", color="green", width=140, height=100)
d.text_box(290, 410, "App Container", font_size=14, color="black")
d.text_box(290, 435, "Sidecar", font_size=14, color="black")

pod2 = d.box(450, 380, "Pod 2", color="green", width=140, height=100)
d.text_box(460, 410, "App Container", font_size=14, color="black")
d.text_box(460, 435, "Sidecar", font_size=14, color="black")

pod3 = d.box(620, 380, "Pod 3", color="green", width=140, height=100)
d.text_box(630, 410, "App Container", font_size=14, color="black")
d.text_box(630, 435, "Sidecar", font_size=14, color="black")

# ConfigMap and Secret
configmap = d.box(280, 550, "ConfigMap", color="cyan", width=140)
secret = d.box(450, 550, "Secret", color="red", width=140)

# PersistentVolumeClaim
pvc = d.box(620, 550, "PersistentVolumeClaim", color="yellow", width=140, height=70)

# Connections
d.arrow_between(ingress, service)
d.arrow_between(service, pod1)
d.arrow_between(service, pod2)
d.arrow_between(service, pod3)

# ConfigMap and Secret to pods
d.arrow_between(configmap, pod1, from_side="top", to_side="bottom")
d.arrow_between(configmap, pod2, from_side="top", to_side="bottom")
d.arrow_between(secret, pod2, from_side="top", to_side="bottom")
d.arrow_between(secret, pod3, from_side="top", to_side="bottom")

# PVC to pods
d.arrow_between(pvc, pod3, from_side="top", to_side="bottom")

# External connections
d.arrow_between(registry, pod1, "pull")
d.arrow_between(monitoring, pod1, "metrics")
d.arrow_between(monitoring, pod2, "metrics")

d.save("gallery_output/deployment.excalidraw")
print("Created: gallery_output/deployment.excalidraw")
