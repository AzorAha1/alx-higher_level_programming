#!/usr/bin/node
const thearray = require('./100-data').list;
console.log(thearray);
const newarray = thearray.map((number, index) => number * index);
console.log(newarray);
