#!/usr/bin/python3
"""takes url and an email sends a post request with email as parameter"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = sys.argv[2]
    paramset = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url=url, data=paramset, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
