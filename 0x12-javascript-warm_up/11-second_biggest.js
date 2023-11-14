#!/usr/bin/node

const args = process.argv;
const len = args.length;
if (len <= 3) {
  console.log(0);
} else {
  const sortedArgs = args.sort();
  console.log(sortedArgs[len - 2]);
}
