#!/bin/bash
#sends a post request to url and display the body respounse with variables
curl -s -X "$1" POST -d "email=test@gmail.com&subject=I will always be here from PLD"
