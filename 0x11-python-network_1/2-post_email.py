#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}

    data = urlencode(value).encode('ascii')

    request = Request(url, data)

    with urlopen(request) as response:
        response_data = response.read()
        decode_response_data = response_data.decode('utf-8')

        print(decode_response_data)
