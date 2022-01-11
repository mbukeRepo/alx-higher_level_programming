#!/usr/bin/python3
"""
 finds the id of github user given username and password
 usage: ./10-my_github.py <username> <password>
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
