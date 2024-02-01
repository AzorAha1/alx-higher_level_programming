#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const id = argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach(element => {
      request.get(element, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const thedata = JSON.parse(body);
          console.log(thedata.name);
        }
      });
    });
  }
});
