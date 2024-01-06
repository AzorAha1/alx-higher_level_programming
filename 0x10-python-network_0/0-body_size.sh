#!/bin/bash
#bash sccript that takes url send request and display size of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
