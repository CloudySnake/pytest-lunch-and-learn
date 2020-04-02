from random import random
import requests


class BadData(Exception):
    pass


def add_up(a: [int, float], b: [int, float]) -> [int, float]:
    if isinstance(a, str) or isinstance(b, str):
        raise BadData("Cannot pass strings to add up function")
    return a + b


def totally_cool_api_call(destination_url: str) -> dict:
    """This is definitely a valid function and not something I made up"""
    response = {"url": destination_url,
                "content": random()}
    return response


def add_up_with_api(destination_url: str, start: int) -> [int, float]:
    response = totally_cool_api_call(destination_url)
    to_add = response["content"]
    return start + to_add
