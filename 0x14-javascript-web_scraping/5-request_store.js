#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const urlpath = argv[3];
request.get(`${url}${urlpath}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile('loripsum', body, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
