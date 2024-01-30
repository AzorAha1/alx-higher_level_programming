#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const thefile = argv[2];
const thecontent = argv[3];
fs.writeFile(thefile, thecontent, (error) => {
  if (error) {
    console.log(error);
  }
});
