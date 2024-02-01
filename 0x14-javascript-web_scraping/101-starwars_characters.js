#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const id = argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let index = 0;
    function move () {
      if (index === data.characters.length) {
        return;
      }
      request.get(data.characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const thedata = JSON.parse(body);
          console.log(thedata.name);
          index++;
          move();
        }
      });
    }
    move();
  }
});
