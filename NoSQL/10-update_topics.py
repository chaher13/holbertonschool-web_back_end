#!/usr/bin/env python3
"""
This a a Python function that changes all topics of a school document
based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object where the school documents are stored.
        name (str): The name of the school to update.
        topics (list): A list of strings representing the new topics to be set for the school.

    Returns:
        None

    Example Usage:
        update_topics(mongo_collection, "School A", ["Math", "Science", "History"])

    This code will update the topics of the school document with the name "School A" in the `mongo_collection` collection. The new topics will be ["Math", "Science", "History"].
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
