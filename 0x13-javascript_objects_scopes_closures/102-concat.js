#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

const contentA = fs.readFileSync(args[2], 'utf-8');
const contentB = fs.readFileSync(args[3], 'utf-8');

const contentAB = contentA + contentB;

fs.writeFileSync(args[4], contentAB, 'utf-8');
