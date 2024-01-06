#!/bin/bash
#send a GET request to the URL and displays the body of the response
curl -s $1 | grep -i HTTP1.1/200
