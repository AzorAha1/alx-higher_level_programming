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
      if (element.completed === true) {
        if (!counter[element.userId]) {
          counter[element.userId] = 1;
        } else {
          counter[element.userId]++;
        }
      }
    });
    console.log(counter);
  }
});
