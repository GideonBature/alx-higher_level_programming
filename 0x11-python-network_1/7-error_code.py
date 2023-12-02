#!/usr/bin/python3
"""sends request to the URL
usage: ./7-error_code.py <url>
returns: displays body of the response
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(response.status_code))
