#!/usr/bin/python3
"""sends a POST request to the passed URL
usage: ./6-post_email.py <url> <email>
returns: body of the response
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    print(response.text)
