#!/bin/bash
# sends request to a url and display only status code
curl -s $1 -o /dev/null -w %{http_code}
