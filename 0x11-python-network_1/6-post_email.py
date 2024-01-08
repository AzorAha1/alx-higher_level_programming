#!/usr/bin/python3
"""take url and email ans set a post request with email as param"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    with requests.post(url=url, data=data) as response:
        print(response.text)
