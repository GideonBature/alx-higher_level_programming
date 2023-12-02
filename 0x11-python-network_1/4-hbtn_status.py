#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
usage: ./4-hbtn_status.py
"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    body = response.content

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body.decode('utf-8')}")
