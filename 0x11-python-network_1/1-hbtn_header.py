#!/usr/bin/python3
"""
   fetches header on response
   usage: ./1-hbtn_header.py <url>
   res.headers.get(<header>)
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
