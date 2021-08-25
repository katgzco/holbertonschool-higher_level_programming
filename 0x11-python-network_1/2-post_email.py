#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a 
    POST request to the passed URL
    with the email as a parameter, and displays the body of the response 
    """
if __name__ == "__main__":

    from urllib import request, parse
    from sys import argv

    req = argv[1]
    information_to_pass = argv[2]

    values = {'email': information_to_pass}
    data = parse.urlencode(values)
    data = data.encode('utf8')

    req = request.Request(req, data)

    with request.urlopen(req) as response:
        response = response.read().decode('utf8')

    print(response)
