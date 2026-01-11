#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create ETL data pipeline diagram
d = Diagram()

# Title
d.text_box(350, 30, "ETL Data Pipeline", font_size=24)

# Data Sources (left, vertical stack)
d.text_box(100, 100, "Data Sources", font_size=18, color="black")
api = d.box(80, 140, "API", color="cyan", width=100, height=60)
database = d.box(80, 230, "Database", color="green", width=100, height=60)
s3 = d.box(80, 320, "S3", color="orange", width=100, height=60)

# Ingestion Layer
d.text_box(280, 100, "Ingestion", font_size=18, color="black")
kafka = d.box(260, 180, "Kafka", color="violet", width=120, height=100)

# Processing Layer
d.text_box(480, 100, "Processing", font_size=18, color="black")
transform = d.box(440, 140, "Transform", color="blue", width=120, height=60)
validate = d.box(440, 220, "Validate", color="blue", width=120, height=60)
enrich = d.box(440, 300, "Enrich", color="blue", width=120, height=60)

# Data Warehouse
d.text_box(680, 100, "Storage", font_size=18, color="black")
snowflake = d.box(660, 180, "Snowflake\nData Warehouse", color="teal", width=140, height=100)

# Analytics Layer
d.text_box(900, 100, "Analytics", font_size=18, color="black")
dashboards = d.box(880, 140, "Dashboards", color="yellow", width=120, height=60)
reports = d.box(880, 220, "Reports", color="yellow", width=120, height=60)
ml = d.box(880, 300, "ML Models", color="red", width=120, height=60)

# Connections - Sources to Kafka
d.arrow_between(api, kafka, "stream")
d.arrow_between(database, kafka, "CDC")
d.arrow_between(s3, kafka, "batch")

# Kafka to Processing
d.arrow_between(kafka, transform, "")
d.arrow_between(kafka, validate, "")
d.arrow_between(kafka, enrich, "")

# Processing to Warehouse
d.arrow_between(transform, snowflake, "")
d.arrow_between(validate, snowflake, "")
d.arrow_between(enrich, snowflake, "")

# Warehouse to Analytics
d.arrow_between(snowflake, dashboards, "")
d.arrow_between(snowflake, reports, "")
d.arrow_between(snowflake, ml, "")

d.save("gallery_output/data_flow.excalidraw")
print("✓ Created: gallery_output/data_flow.excalidraw")
