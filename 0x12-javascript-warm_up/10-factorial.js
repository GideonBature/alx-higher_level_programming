#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num) || num === undefined) {
  console.log(1);
} else {
  function factorial (num) {
    if (num === 0 || num === 1) {
      return (1);
    }
    return (num * factorial(num - 1));
  }
  const result = factorial(num);
  console.log(result);
}
