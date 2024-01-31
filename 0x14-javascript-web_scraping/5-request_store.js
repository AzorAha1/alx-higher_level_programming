#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const urlpath = argv[3];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(urlpath, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
