#!/bin/bash
# sends a json post request to url and display body of the response
curl -s -H "Content-Type: application/json" -d '$(cat "$2")' $1
