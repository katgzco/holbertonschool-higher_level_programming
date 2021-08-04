#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
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
