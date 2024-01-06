#!/bin/bash
#sends a post request to url and display the body respounse with variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
