data_sources = [
    {"name": "analytics_pg", "type": "PostgreSQL", "is_active": True, "record_count": 12000},
    {"name": "legacy_mysql", "type": "MySQL", "is_active": False, "record_count": 0},
    {"name": "events_mongo", "type": "MongoDB", "is_active": True, "record_count": 45000},
    {"name": "logs_pg", "type": "PostgreSQL", "is_active": True, "record_count": 8000}
]

for source in data_sources:
    if source["is_active"] == True and source['record_count'] > 10000:
        print(f"Ready to extract: {source['name']} ({source['record_count']} records)")
    elif source['is_active'] == False:
        print(f"Skipped inactive source: {source['name']}")