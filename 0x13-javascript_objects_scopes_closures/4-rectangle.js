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

  rotate () {
    const auxiliarChange = this.width;
    this.width = this.height;
    this.height = auxiliarChange;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
