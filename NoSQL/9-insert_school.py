#!/usr/bin/env python3
"""
This is a Python function that inserts a new document
in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (MongoDB collection object): The MongoDB collection where the document will be inserted.
        **kwargs (keyword arguments): The keyword arguments used to create the new document.

    Returns:
        string: The ID of the inserted document.
    """

    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
