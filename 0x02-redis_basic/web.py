#!/usr/bin/env python3
"""This module defines the function get_page."""

import redis
import requests
from typing import Callable
from functools import wraps


def requests_count(fn: Callable) -> Callable:
    """This function returns a wrapper function."""

    redis_client = redis.Redis()

    @wraps(fn)
    def wrapper_function(url):
        """
        This function returns the number of requests to a
        particular url.
        """
        key = "count:{}".format(url)
        redis_client.incr(key)

        cached_result = redis_client.get(key)

        if cached_result:
            return cached_result.decode("utf-8")

        result = fn(url)

        redis_client.setex(key, 10, result)

        return result

    return wrapper_function


@requests_count
def get_page(url: str) -> str:
    """
    This function uses the requests module to obtain the
    HTML content of a particular URL and returns it.
    """

    response = requests.get(url)
    html_content = response.text

    return html_content
