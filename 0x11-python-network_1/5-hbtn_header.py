#!/usr/bin/python3
"""
   makes a request and display header(res)
   header: X-Request-Id
   usage: ./5-hbtn_header.py <url>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
