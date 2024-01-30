#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
