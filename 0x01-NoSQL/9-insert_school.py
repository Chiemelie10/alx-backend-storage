#!/usr/bin/env python3
"""This module defines the function insert_school."""


def insert_school(mongo_collection, **kwargs):
    """
    This function inserts a new document in a collection based on kwargs.
    """

    insert_result_object = mongo_collection.insert_one(kwargs)

    return insert_result_object.inserted_id
