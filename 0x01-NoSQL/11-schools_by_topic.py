#!/usr/bin/env python3
"""This module defines the function schools_by_topic."""


def schools_by_topic(mongo_collection, topic):
    """This module returns a list of school having a specific topic."""

    schools = mongo_collection.find({'topics': topic})

    return schools
