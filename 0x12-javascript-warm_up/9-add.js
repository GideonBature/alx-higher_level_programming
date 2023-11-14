#!/usr/bin/node

const args = process.argv;

const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

if (isNaN(num1) || num1 === undefined || isNaN(num2) || num2 === undefined) {
  console.log('NaN');
} else {
  function add (a, b) {
    return (a + b);
  }
  const result = add(num1, num2);
  console.log(result);
}
