#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx_collection = db.nginx

    number_of_documents = nginx_collection.count_documents({})
    print("{} logs".format(number_of_documents))

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for http_method in http_methods:
        count = nginx_collection.count_documents({"method": http_method})
        print("\tmethod {}: {}".format(http_method, count))

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))
