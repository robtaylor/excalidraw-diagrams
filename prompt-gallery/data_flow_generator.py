#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excalidraw-diagrams/scripts"))
from excalidraw_generator import Diagram

# Create an ETL pipeline data flow diagram
d = Diagram()

# Title
d.text_box(280, 20, "ETL Data Pipeline", font_size=28)

# Data Sources (left column)
d.text_box(100, 90, "Data Sources", font_size=20, color="gray")
api = d.box(80, 130, "API", color="cyan", width=120)
database = d.box(80, 220, "Database", color="cyan", width=120)
s3 = d.box(80, 310, "S3", color="cyan", width=120)

# Ingestion Layer
d.text_box(280, 90, "Ingestion", font_size=20, color="gray")
kafka = d.box(260, 200, "Kafka", color="orange", width=120)

# Processing Layer
d.text_box(460, 90, "Processing", font_size=20, color="gray")
transform = d.box(440, 130, "Transform", color="blue", width=120)
validate = d.box(440, 220, "Validate", color="blue", width=120)
enrich = d.box(440, 310, "Enrich", color="blue", width=120)

# Data Warehouse
d.text_box(620, 90, "Storage", font_size=20, color="gray")
snowflake = d.box(600, 200, "Snowflake", color="green", width=120)

# Analytics Layer
d.text_box(780, 90, "Analytics", font_size=20, color="gray")
dashboards = d.box(760, 130, "Dashboards", color="violet", width=120)
reports = d.box(760, 220, "Reports", color="violet", width=120)
ml_models = d.box(760, 310, "ML Models", color="violet", width=120)

# Connections from sources to Kafka
d.arrow_between(api, kafka)
d.arrow_between(database, kafka)
d.arrow_between(s3, kafka)

# Connections from Kafka to Processing
d.arrow_between(kafka, transform)
d.arrow_between(kafka, validate)
d.arrow_between(kafka, enrich)

# Connections from Processing to Snowflake
d.arrow_between(transform, snowflake)
d.arrow_between(validate, snowflake)
d.arrow_between(enrich, snowflake)

# Connections from Snowflake to Analytics
d.arrow_between(snowflake, dashboards)
d.arrow_between(snowflake, reports)
d.arrow_between(snowflake, ml_models)

d.save("gallery_output/data_flow.excalidraw")
print("Created: gallery_output/data_flow.excalidraw")
