#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const thefile = argv[2];
fs.readFile(thefile, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
