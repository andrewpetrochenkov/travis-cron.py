#!/usr/bin/env python
import json
import os
import requests


def request(method, url, data=None, **kwargs):
    """make request and return response"""
    TRAVIS_TOKEN = os.getenv("TRAVIS_TOKEN")
    if "headers" not in kwargs:
        kwargs["headers"] = {}
    kwargs["headers"].update({
        "Authorization": "token %s" % TRAVIS_TOKEN,
        "Travis-API-Version": "3",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    if data is not None:
        data = json.dumps(data)
    r = requests.request(method, url, data=data, **kwargs)
    r.raise_for_status()
    return r
