#!/usr/bin/python3
"""take url send request and display body with status code & error handling"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            print(response.text)
    except requests.HTTPError as errror:
        if requests.status_codes >= 400:
            print(f'Error code: {errror.response.status_code}')