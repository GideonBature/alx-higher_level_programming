#!/usr/bin/node

const FSquare = require('./5-square');

class Square extends FSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) {
        const repeatedC = c.repeat(this.width);
        console.log(repeatedC);
      }
    }
  }
}

module.exports = Square;
