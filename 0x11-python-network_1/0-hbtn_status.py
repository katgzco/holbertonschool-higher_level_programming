#!/usr/bin/python3

"""Python script that fetches https://intranet.hbtn.io/status
    """
if __name__ == "__main__":

    from urllib import request

    req = request.Request('https://intranet.hbtn.io/status')

    with request.urlopen(req) as response:
        response = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
    print('\t- utf8 content: {}'.format(response.decode('utf-8')))
