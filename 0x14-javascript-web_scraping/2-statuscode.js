#!/usr/bin/node
const request = require('request');
const argv = process.argv;
url = argv[2]
request(url, (response) => {
    console.log('code: %d', response.statusCode)
});
