#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
    and displays the body of the response"""

if __name__ == "__main__":

    from urllib import request, error
    from sys import argv

    req = argv[1]

    try:
        with request.urlopen(req) as response:
            response = response.read().decode('utf8')
        print(response)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))

