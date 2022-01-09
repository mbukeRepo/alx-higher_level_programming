#!/usr/bin/python3
"""
   sends a post request to a url
   data: {email: <email>}
   usage: ./2-post_email.py <url> <email>
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data["email"] = sys.argv[2]
    data = urllib.parse.urlencode(data)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
