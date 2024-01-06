#!/bin/bash
#sends a post request to url and display the body respounse with variables
curl -sL "$1" -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
