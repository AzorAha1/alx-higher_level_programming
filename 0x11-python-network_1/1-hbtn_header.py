#!/usr/bin/python3
"""takes url and sends a request to the url display the value"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url=url) as response:
        print(response.getheader(name='X-Request-Id'))
