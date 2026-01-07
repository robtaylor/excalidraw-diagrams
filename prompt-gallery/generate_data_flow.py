#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create ETL data pipeline diagram
d = Diagram()

# Add title
d.text_box(250, 30, "ETL Data Pipeline", font_size=24)

# Stage 1: Data Sources (left)
d.text_box(50, 100, "Data Sources", font_size=20, color="gray")
api = d.box(50, 140, "API", width=120, height=60, color="gray")
database = d.box(50, 220, "Database", width=120, height=60, color="gray")
s3 = d.box(50, 300, "S3", width=120, height=60, color="gray")

# Stage 2: Ingestion Layer
d.text_box(240, 100, "Ingestion", font_size=20, color="orange")
kafka = d.box(240, 200, "Kafka", width=140, height=100, color="orange")

# Stage 3: Processing
d.text_box(450, 100, "Processing", font_size=20, color="blue")
transform = d.box(450, 150, "Transform", width=140, height=60, color="blue")
validate = d.box(450, 230, "Validate", width=140, height=60, color="blue")
enrich = d.box(450, 310, "Enrich", width=140, height=60, color="blue")

# Stage 4: Data Warehouse
d.text_box(660, 100, "Storage", font_size=20, color="green")
warehouse = d.box(660, 200, "Snowflake\nData Warehouse", width=150, height=100, color="green")

# Stage 5: Analytics
d.text_box(880, 100, "Analytics", font_size=20, color="violet")
dashboards = d.box(880, 150, "Dashboards", width=130, height=60, color="violet")
reports = d.box(880, 230, "Reports", width=130, height=60, color="violet")
ml = d.box(880, 310, "ML Models", width=130, height=60, color="violet")

# Connections - Sources to Kafka
d.arrow_between(api, kafka)
d.arrow_between(database, kafka)
d.arrow_between(s3, kafka)

# Kafka to Processing
d.arrow_between(kafka, transform)
d.arrow_between(kafka, validate)
d.arrow_between(kafka, enrich)

# Processing to Warehouse
d.arrow_between(transform, warehouse)
d.arrow_between(validate, warehouse)
d.arrow_between(enrich, warehouse)

# Warehouse to Analytics
d.arrow_between(warehouse, dashboards)
d.arrow_between(warehouse, reports)
d.arrow_between(warehouse, ml)

d.save("gallery_output/data_flow.excalidraw")
print("Created: gallery_output/data_flow.excalidraw")
