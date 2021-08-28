#!/usr/bin/python3

"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":

    dict_ = {'q': ''}
    if len(sys.argv) == 2:
        dict_ = {'q': sys.argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=dict_)
    if 'application/json' not in response.headers.get('Content-Type'):
        print('Not a valid JSON')
    if response.json():
        r_json = response.json()
        print('[{}] {}'.format(r_json.get('id'), r_json.get('name')))
    else:
        print('No result')
