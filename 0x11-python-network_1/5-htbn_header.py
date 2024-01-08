#!/usr/bin/python3
"""take url send a request to url and get variable"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers['X-Request-Id'])