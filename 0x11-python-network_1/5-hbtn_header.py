#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""

import requests
import sys

if __name__ == "__main__":

    host = sys.argv[1]

    response = requests.get(host)
    print(response.headers.get('X-Request-Id'))
