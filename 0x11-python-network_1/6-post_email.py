#!/usr/bin/python3
""" 
   making a post request with requests module 
   data : {email: "<data>"}
   usage: ./6-post_email.py <url> <email>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email":sys.argv[2]}

    res = requests.post(url, data=values)
    print(res.text)
