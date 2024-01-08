#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        body_utf8 = body.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body}")
