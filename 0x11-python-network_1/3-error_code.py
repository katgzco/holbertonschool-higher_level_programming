#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
    and displays the body of the response"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    req = sys.argv[1]

    try:
        with urllib.request.urlopen(req) as response:
            response = response.read().decode('utf8')
            print(response)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
