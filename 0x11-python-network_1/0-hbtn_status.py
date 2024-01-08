#!/usr/bin/python3
# this will fetch a certain site
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print(response.read())