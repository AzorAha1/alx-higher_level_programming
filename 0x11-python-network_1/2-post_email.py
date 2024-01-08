#!/usr/bin/python3
"""takes url and an email sends a post request with email as parameter"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    with urllib.request.urlopen(url) as response:
        print(dir(response))