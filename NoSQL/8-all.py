#!/usr/bin/env python3
"""
This is a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object representing the MongoDB collection.

    Returns:
        list: A list containing all the documents retrieved from the MongoDB collection. If there are no documents in the collection, an empty list is returned.
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
