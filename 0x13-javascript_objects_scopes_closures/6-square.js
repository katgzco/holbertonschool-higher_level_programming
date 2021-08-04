#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let column = this.height;
      while (column > 0) {
        console.log('C'.repeat(this.width));
        column--;
      }
    } else {
        super.print();
    }
  }
};

module.exports = Square;
