#!/usr/bin/python3
"""takes a request and displays body while managing error"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))