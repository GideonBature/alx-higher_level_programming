#!/usr/bin/node
// a script that gets the contents of
// a webpage and stores it in a file.
const process = require('process');
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
