#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    req = argv[1]

    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
