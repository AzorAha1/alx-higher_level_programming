#!/usr/bin/node

const LastSquare = require('./5-square');

class Square extends LastSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          row += c;
        } else {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
}
module.exports = Square;
