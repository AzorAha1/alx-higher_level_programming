#!/usr/bin/python3
"""take url send request and display body with status code & error handling"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2:
        letter = ""   
    letter = sys.argv[1]
    if letter:
        data = {'q':letter}
    else:
        data = {'q':""}
    response = requests.post(data=data, url='http://0.0.0.0:5000/search_user')
    try:
        json_code = response.json();
    except ValueError:
        print("Not a valid JSON")
    if json_code == {}:
        print('No result')
    else:
        print(f"[{response.get('id')}] {response.get('name')}")
    
    
    