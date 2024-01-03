#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let sum = 0;
    const jsonBody = JSON.parse(body);
    const len = jsonBody.results.length;
    for (let i = 0; i < len; i++) {
      for (let j = 0; j < jsonBody.results[i].characters.length; j++) {
        if (jsonBody.results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          sum += 1;
        }
      }
    }
    console.log(sum);
  }
});
