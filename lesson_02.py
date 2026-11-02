source_databases = ["PostgreSQL", "MySQL", "MongaDB"]

pipleline_config = {
    "pipeline" : 1001,
    "source" : source_databases[0],
    "batch_size": 10000,
    "is_active" : True
}

print(pipleline_config["pipeline"])
print(pipleline_config["source"])
print(pipleline_config["batch_size"])
print(pipleline_config["is_active"])

