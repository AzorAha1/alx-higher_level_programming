#!/bin/bash
# sends a json post request to url and display body of the response
curl -s -X POST -H "Content-Type: application/json" -d '{"key": "value"}' $1
