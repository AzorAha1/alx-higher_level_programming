#!/usr/bin/python3
# this will fetch a certain site
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    body_utf8 = response.decode('utf-8')
    print(f"- type: {type(body_utf8)}")