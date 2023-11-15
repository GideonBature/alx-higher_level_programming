#!/usr/bin/node

exports.esrever = function (list) {
  const lenList = list.length;

  for (let i = 0; i < Math.floor(lenList / 2); i++) {
    const temp = list[i];
    list[i] = list[lenList - i - 1];
    list[lenList - i - 1] = temp;
  }
  return (list);
};
