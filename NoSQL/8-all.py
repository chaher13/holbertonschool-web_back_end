#!/usr/bin/env python3
"""
This is a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):

    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
