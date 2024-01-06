#!/bin/bash
#takes a url and shows the http methods the server will accept
curl -sI "$1" | grep -i "Allow" | awk '{print $2}'
