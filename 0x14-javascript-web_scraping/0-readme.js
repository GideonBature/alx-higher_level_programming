#!/usr/bin/node
// script that reads and prints
// the content of a file
const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
