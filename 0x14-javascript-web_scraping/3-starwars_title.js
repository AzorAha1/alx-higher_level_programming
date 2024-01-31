#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const id = argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const thefilm = JSON.parse(body);
    console.log(thefilm.title);
  }
});
