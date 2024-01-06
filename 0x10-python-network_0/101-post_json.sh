#!/bin/bash
# sends a json post request to url and display body of the response
curl -sI -X POST -H "Content-Type: $2" -d @"$3" $1