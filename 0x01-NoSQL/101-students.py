#!/usr/bin/env python3
""" Python function that returns 
all students sorted by average score
"""


def top_students(mongo_collection):
    """function that returns students by average
    score
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])