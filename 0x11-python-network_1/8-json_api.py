#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py <letter>
returns: [<id>] <name>
"""
import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
        payload = {'q': q}
    except IndexError:
        print("No result")
        sys.exit()

    response = requests.post(url, payload)

    try:
        r_json = response.json()
        if r_json == {}:
            print("No result")
        else:
            print(f"[{r_json.get('id')}] {r_json.get('name')}")
    except ValueError:
        print("Not a valid JSON")
