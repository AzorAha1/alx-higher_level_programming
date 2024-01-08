#!/usr/bin/python3
"""take url send a request to url and get variable"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    with requests.get(url) as response:
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
