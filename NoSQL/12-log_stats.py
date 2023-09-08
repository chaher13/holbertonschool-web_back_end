#!/usr/bin/env python3
"""
This is a Python script that provides some stats
about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents
with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
one line with the number of documents with:
method=GET
path=/status
"""
import pymongo


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["logs"]
collection = db["nginx"]

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method})
                 for method in methods}

status_check_count = collection.count_documents({"method": "GET",
                                                 "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")

mongo_client.close()
