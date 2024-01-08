#!/usr/bin/python3
"""takes url and an email sends a post request with email as parameter"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = sys.argv[2]
    
    paramset = urllib.parse.urlencode({'email':email}).encode('utf-8')
    request_type = urllib.request.Request(url=url, data=paramset,method='POST')
    with urllib.request.urlopen(request_type) as response:
        print(type(response.read()))