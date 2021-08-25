#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a 
POST request to the passed URL
with the email as a parameter, and displays the body of the response"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    req = sys.argv[1]
    information_to_pass = sys.argv[2]

    values = {'email': information_to_pass}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(req, data)

    with urllib.request.urlopen(req) as response:
        response = response.read().decode('utf8')
        print(response)
