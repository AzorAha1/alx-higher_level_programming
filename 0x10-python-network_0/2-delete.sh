#!/bin/bash
#sends a DELETE request to the url passed and displays the body of response
curl -sI "$1" | grep -i "allow" | awk '{print $2}'
