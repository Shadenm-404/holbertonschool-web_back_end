#!/usr/bin/env python3
"""Return schools by topic"""

def schools_by_topic(mongo_collection, topic):
    """Find schools with a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
