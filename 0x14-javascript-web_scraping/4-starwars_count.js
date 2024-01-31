#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];
let sum = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(element => {
      const url = element.characters;
      url.forEach(element => {
        if (element.endsWith('/18/')) {
          sum++;
        }
      });
    });
    console.log(sum);
  }
});
