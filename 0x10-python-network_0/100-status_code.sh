#!/bin/bash
# sends request to a url and display only status code
curl -s $1 -w %{http_code}