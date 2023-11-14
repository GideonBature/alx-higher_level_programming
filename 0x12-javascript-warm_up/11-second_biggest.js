#!/usr/bin/node

const args = process.argv;
const len = args.length;
if (len <= 3) {
	console.log(0);
} else {
	const intArray = args.map(str => parseInt(str));
	const sortedIntArray = intArray.sort((a, b) => b - a);
	console.log(sortedIntArray[3]);
}
