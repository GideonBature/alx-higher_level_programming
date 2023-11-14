#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  let count = 1;
  while (count <= x) {
    console.log('C is fun');
    count++;
  }
}
