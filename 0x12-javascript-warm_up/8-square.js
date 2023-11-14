#!/usr/bin/node

const args = process.argv;

const x = parseInt(args[2]);

if (isNaN(x) || x === undefined) {
  console.log('Missing size');
} else {
  let size = 1;
  const string = 'X';
  while (size <= x) {
    const repeatedString = string.repeat(x);
    console.log(repeatedString);
    size++;
  }
}
