#!/usr/bin/python3
"""Script displays the value of variable X-Request-Id
usage: ./5-hbtn_header.py <url>
returns: value of X-Request-Id
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    print(response.headers['X-Request-Id'])
