#!/usr/bin/python3
""" 
   sends a req and prints error if raised
   usage: ./3-error_code.py
   raised error: urllib.error.HTTPError
"""

import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
