#!/usr/bin/python3
"""take url send request and display body with status code & error handling"""
if __name__ == "__main__":
    import requests
    import sys
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    data = {'q': letter} if letter else {'q': ""}
    response = requests.post(url='http://0.0.0.0:5000/search_user', data=data)
    try:
        json_code = response.json()
        if not json_code:
            print('No result')
        else:
            print(f"[{json_code.get('id')}] {json_code.get('name')}")
    except ValueError:
        print("Not a valid JSON")
