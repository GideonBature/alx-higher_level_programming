#!/usr/bin/node

const args = process.argv;
const count = args.length;
if (count <= 2) { console.log('No argument'); } else if (count === 3) { console.log('Argument found'); } else if (count > 3) { console.log('Arguments found'); }
