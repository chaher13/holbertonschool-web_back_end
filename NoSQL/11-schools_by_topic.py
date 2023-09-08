#!/usr/bin/env python3
"""
This is  a Python function that returns
the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic in their "topics" field.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object to search through.
        topic (str): The topic to search for in the "topics" field of the documents.

    Returns:
        list: A list of schools that match the specified topic.

    Example Usage:
        # Assuming we have a MongoDB collection named "schools" with documents like:
        # {
        #   "_id": ObjectId("60a5e8e1e5d5e4a1c4e7e3f2"),
        #   "name": "School A",
        #   "topics": ["Math", "Science"]
        # }
        # {
        #   "_id": ObjectId("60a5e8e1e5d5e4a1c4e7e3f3"),
        #   "name": "School B",
        #   "topics": ["Science", "History"]
        # }

        # Create a connection to the MongoDB server
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Access the "schools" collection
        db = client["mydatabase"]
        collection = db["schools"]

        # Call the schools_by_topic function to get schools with the topic "Science"
        result = schools_by_topic(collection, "Science")

        # Print the result
        print(result)
        # Output: [{'_id': ObjectId('60a5e8e1e5d5e4a1c4e7e3f2'), 'name': 'School A', 'topics': ['Math', 'Science']}, {'_id': ObjectId('60a5e8e1e5d5e4a1c4e7e3f3'), 'name': 'School B', 'topics': ['Science', 'History']}]
    """

    schools = []
    for school in mongo_collection.find():
        if "topics" in school and topic in school["topics"]:
            schools.append(school)
    return schools
