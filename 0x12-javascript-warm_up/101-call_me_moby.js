#!/usr/bin/node

function theFunction () {
  return 'C is fun';
}

exports.callMeMoby = function (x, theFunction) {
  let count;
  for (count = 0; count < x; count++) {
    theFunction();
  }
};
