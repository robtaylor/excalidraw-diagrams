#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create an ETL data pipeline diagram
d = Diagram()

# Title
d.text_box(300, 30, "ETL Data Pipeline", font_size=24)

# Data Sources
api_source = d.box(50, 120, "API", color="gray", width=100)
db_source = d.box(50, 220, "Database", color="gray", width=100)
s3_source = d.box(50, 320, "S3", color="gray", width=100)

# Ingestion Layer
kafka = d.box(250, 200, "Kafka\nIngestion", color="orange", width=120, height=80)

# Processing Layer
transform = d.box(450, 120, "Transform", color="blue", width=120)
validate = d.box(450, 220, "Validate", color="blue", width=120)
enrich = d.box(450, 320, "Enrich", color="blue", width=120)

# Data Warehouse
warehouse = d.box(650, 200, "Snowflake\nData Warehouse", color="green", width=140, height=80)

# Analytics
dashboards = d.box(850, 120, "Dashboards", color="violet", width=120)
reports = d.box(850, 220, "Reports", color="violet", width=120)
ml = d.box(850, 320, "ML Models", color="violet", width=120)

# Connections - Sources to Kafka
d.arrow_between(api_source, kafka, "stream")
d.arrow_between(db_source, kafka, "CDC")
d.arrow_between(s3_source, kafka, "batch")

# Kafka to Processing (Spark)
d.arrow_between(kafka, transform, "")
d.arrow_between(kafka, validate, "")
d.arrow_between(kafka, enrich, "")

# Processing to Warehouse
d.arrow_between(transform, warehouse, "")
d.arrow_between(validate, warehouse, "")
d.arrow_between(enrich, warehouse, "")

# Warehouse to Analytics
d.arrow_between(warehouse, dashboards, "SQL")
d.arrow_between(warehouse, reports, "SQL")
d.arrow_between(warehouse, ml, "feature")

d.save("gallery_output/data_flow.excalidraw")
print("Created: data_flow.excalidraw")
