#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let count;
  for (count = 0; count < x; count++) {
    theFunction();
  }
};
