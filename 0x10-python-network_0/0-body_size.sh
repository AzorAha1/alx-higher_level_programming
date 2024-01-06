#!/usr/bin/env bash
#bash sccript that takes url send request and display size of the response
curl -sI http://www.example.com | grep -i Content-Length | awk '{print $2}'
