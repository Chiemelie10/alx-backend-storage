#!/usr/bin/env python3
"""This script defines the function list_all."""


def list_all(mongo_collection):
    """This function lists all documents in a collection."""

    documents = list(mongo_collection.find())

    return documents
