# Lesson 1: Data Engineering Variables
source_system = "PostgreSQL"
batch_size = 5000
is_successful = True

print(f"Pipeline initialized for source: {source_system}")
print(f"Batch size: {batch_size} records")
print(f"Execution status: {is_successful}")

# A list of database tables to extract
tables_to_extract = ["users", "orders", "payments"]

# 1. Lists: Ordered Sequences:->

# Accessing items by index
print(tables_to_extract[0])  # Output: users
print(tables_to_extract[2]) # Output: payments

# Adding a new table to the list
tables_to_extract.append("inventory")
print(tables_to_extract)    # Outputs: ['users', 'orders', 'payments', 'inventory']

# 2. Dictionaries: Key-Value Pairs
# A dictionary stores data mapped as key: value, enclosed in curly braces {}
# In data engineering, a dictionary represents a single row/record extracted from a database table or a JSON API response.   
# You access values using the key name, not numerical indices.

user_record = {
    "user_id": 4012,
    "username": "amaan99",
    "is_active": True,
    "total_spend": 248.50
}

# Accessing values via keys
print(user_record["username"]) # Outpurs : amaan99
print(user_record["total_spend"]) # Outputs: 248.50

# 3. Combining Both: A Dataset (List of Dictionaries)
# In Python, a mini tabular dataset (like a small database table or JSON payload) is typically 
# structured as a list of dictionaries:

# A batch of incoming user records
users_batch = [
    {"user_id":1, "username": "alice", "active": True},
    {"user_id":2, "username": "bob", "active": False},
    {"user_id":3, "username": "charlie", "active": True},
]

# Accessing the second user's username
print(users_batch[1]["username"]) #Outputs: bob