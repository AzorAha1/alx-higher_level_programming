#!/usr/bin/python3
"""using requests module to fetch url"""
if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as response:
        responsetostr = response.text
        print('Body response:')
        print(f'\t- type: {type(responsetostr)}')
        print(f'\t- content: {responsetostr}')
