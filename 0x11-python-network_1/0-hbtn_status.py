#!/usr/bin/python3
import urllib.request
# this will fetch a certain site
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    body_utf8 = body.decode('utf-8')
    type = f"- type: {type(body)}"
    content = f"- content: {body}"
    utf8_content = f"- utf8 content: {body}"
    print(f'''
Body response:
    {type}
    {content}
    {utf8_content}
'''.strip()
)
