#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let column = this.height;
    while (column > 0) {
      console.log('X'.repeat(this.width));
      column--;
    }
  }
}

module.exports = Rectangle;
