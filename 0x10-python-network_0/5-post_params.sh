#!/bin/bash
#sends a post request to url and display the body respounse with variables
curl -sL -X POST "$1" -d "email=test@gmail.com&subject: I will always be here for PLD"
