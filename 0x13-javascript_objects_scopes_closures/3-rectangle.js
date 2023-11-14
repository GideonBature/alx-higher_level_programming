#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const str = 'X';
      const repeatedStr = str.repeat(this.width);
      console.log(repeatedStr);
    }
  }
}

module.exports = Rectangle;
