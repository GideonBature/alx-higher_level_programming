#!/usr/bin/python3
"""takes in url, sends a request to the url
usage: ./3-error_code.py <url>
return: body of response(utf-8)
"""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
