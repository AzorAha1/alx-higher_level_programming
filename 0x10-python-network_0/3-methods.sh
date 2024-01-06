#!/bin/bash
#takes a url and shows the http methods the server will accept
curl -sL -X OPTIONS $1 -i
