#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const counter = {};
    data.forEach(element => {
      if (!counter[element.userId]) {
        counter[element.userId] = 0;
      }
      if (element.completed === true) {
        counter[element.userId]++;
      }
    });
    console.log(counter);
  }
});
