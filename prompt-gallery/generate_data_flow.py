#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# ETL Data Pipeline
d = Diagram()

# Data Sources stage
api_src = d.box(80, 100, "API", color="orange")
db_src = d.box(80, 200, "Database", color="orange")
s3_src = d.box(80, 300, "S3", color="orange")

# Ingestion layer
kafka = d.box(280, 200, "Kafka\n(Ingestion)", color="yellow", width=120)

# Processing stage
transform = d.box(480, 100, "Transform", color="violet")
validate = d.box(480, 200, "Validate", color="violet")
enrich = d.box(480, 300, "Enrich", color="violet")

# Data Warehouse
snowflake = d.box(680, 200, "Snowflake\n(Data Warehouse)", color="cyan", width=140)

# Analytics layer
dashboards = d.box(900, 100, "Dashboards", color="blue")
reports = d.box(900, 200, "Reports", color="blue")
ml_models = d.box(900, 300, "ML Models", color="blue")

# Connections - Data sources to Kafka
d.arrow_between(api_src, kafka)
d.arrow_between(db_src, kafka)
d.arrow_between(s3_src, kafka)

# Kafka to Processing
d.arrow_between(kafka, transform)
d.arrow_between(kafka, validate)
d.arrow_between(kafka, enrich)

# Processing to Warehouse
d.arrow_between(transform, snowflake)
d.arrow_between(validate, snowflake)
d.arrow_between(enrich, snowflake)

# Warehouse to Analytics
d.arrow_between(snowflake, dashboards)
d.arrow_between(snowflake, reports)
d.arrow_between(snowflake, ml_models)

d.save("gallery_output/data_flow.excalidraw")
print("Created: gallery_output/data_flow.excalidraw")
