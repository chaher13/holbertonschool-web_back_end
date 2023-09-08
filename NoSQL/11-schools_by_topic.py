#!/usr/bin/env python3
"""
This is  a Python function that returns
the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):

    schools = []
    for school in mongo_collection.find():
        if "topics" in school and topic in school["topics"]:
            schools.append(school)
    return schools
