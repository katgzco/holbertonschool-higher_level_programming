#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c && typeof c === 'string' && c.length === 1) {
      let column = this.height;
      while (column > 0) {
        console.log(c.repeat(this.width));
        column--;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
