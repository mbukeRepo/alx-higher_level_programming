#!/usr/bin/python3
"""
 Sends a post request to a url
 usage: ./8-json_api.py <letter>
"""

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    values = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=values)

    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
