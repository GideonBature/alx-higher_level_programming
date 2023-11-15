#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const lenList = list.length;
  let count = 0;

  for (let i = 0; i < lenList; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
