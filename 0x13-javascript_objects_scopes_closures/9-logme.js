#!/usr/bin/node

let itemCount = 0;
exports.logMe = function (item) {
  console.log(`${itemCount}: ${item}`);
  itemCount++;
};
