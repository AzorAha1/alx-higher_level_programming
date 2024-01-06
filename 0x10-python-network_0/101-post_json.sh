#!/bin/bash
# sends a json post request to url and display body of the response
curl -s -X POST -H "Content-Type: application/json" -d '{"key1": "value1", "key2":"value2"}' $1