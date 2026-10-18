#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create a data flow diagram for ETL pipeline
d = Diagram()

# Title
d.text_box(350, 30, "ETL Data Pipeline", font_size=24, color="black")

# Data Sources (left column, different colors)
api = d.box(50, 100, "API", width=120, height=60, color="gray")
database = d.box(50, 200, "Database", width=120, height=60, color="gray")
s3 = d.box(50, 300, "S3", width=120, height=60, color="gray")

# Ingestion Layer
kafka = d.box(250, 180, "Kafka\nIngestion", width=140, height=80, color="blue")

# Processing Layer (middle column, different stages)
transform = d.box(470, 100, "Transform", width=130, height=60, color="orange")
validate = d.box(470, 200, "Validate", width=130, height=60, color="orange")
enrich = d.box(470, 300, "Enrich", width=130, height=60, color="orange")

# Processing label
d.text_box(450, 70, "Spark Processing", font_size=16, color="orange")

# Data Warehouse
snowflake = d.box(680, 180, "Snowflake\nData Warehouse", width=160, height=80, color="green")

# Analytics Layer (right column)
dashboards = d.box(920, 100, "Dashboards", width=140, height=60, color="violet")
reports = d.box(920, 200, "Reports", width=140, height=60, color="violet")
ml = d.box(920, 300, "ML Models", width=140, height=60, color="violet")

# Connections - Sources to Kafka
d.arrow_between(api, kafka, "stream")
d.arrow_between(database, kafka, "CDC")
d.arrow_between(s3, kafka, "batch")

# Kafka to Processing
d.arrow_between(kafka, transform)
d.arrow_between(kafka, validate)
d.arrow_between(kafka, enrich)

# Processing to Warehouse
d.arrow_between(transform, snowflake)
d.arrow_between(validate, snowflake)
d.arrow_between(enrich, snowflake)

# Warehouse to Analytics
d.arrow_between(snowflake, dashboards, "query")
d.arrow_between(snowflake, reports, "query")
d.arrow_between(snowflake, ml, "training")

# Save
output_path = "/home/runner/work/excalidraw-diagrams/excalidraw-diagrams/gallery_output/data_flow.excalidraw"
d.save(output_path)
print(f"Created: {output_path}")
print(f"Element count: {len(d.elements)}")
