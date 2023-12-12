#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        if (c !== undefined) {
          row += 'C';
        } else if (c === undefined) {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
}
module.exports = Square;
