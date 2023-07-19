#!/usr/bin/env python3
"""This module defines the class Cache."""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """
    This class defines the attributes and methods necessary to
    cache data using Redis.
    """

    def __init__(self):
        """
        This contructor defines ensures that the class Cache
        connects to the redis database when an instance of the
        class created.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method generates a random key using uuid. It stores the
        input data in Redis using the random key and return the key.
        """

        key = str(uuid4())
        self._redis.set(key, data)

        return key
