#!/usr/bin/env python3
"""This module defines the function get_page."""

import redis
import requests
import time
from typing import Callable
from functools import wraps


def cached_with_redis(expiration: int):
    """Decorator function."""

    def requests_count(fn: Callable) -> Callable:
        """This function returns a wrapper function."""

        redis_client = redis.Redis()

        @wraps(fn)
        def wrapper_function(url):
            """
            This function returns the number of requests to a
            particular url.
            """
            key = "cache:{}".format(url)

            cached_result = redis_client.get(key)

            if cached_result:
                return cached_result.decode("utf-8")

            result = func(url)

            redis_client.setex(key, expiration, result)

            return result

        return wrapper_function

    return requests_count


def track_access(fn: Callable) -> Callable:
    """This function returns a wrapper function."""

    redis_client = redis.Redis()

    @wraps(fn)
    def wrapper(url):
        count_key = "count:{}".format(url)
        redis_client.incr(count_key)

        return fn(url)

    return wrapper


@cached_with_redis(expiration=10)
@track_access
def get_page(url: str) -> str:
    """
    This function uses the requests module to obtain the
    HTML content of a particular URL and returns it.
    """

    response = requests.get(url)
    html_content = response.text

    return html_content
