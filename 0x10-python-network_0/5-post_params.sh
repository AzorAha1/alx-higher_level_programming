#!/bin/bash
#sends a post request to url and display the body respounse with variables
curl -s -X POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
