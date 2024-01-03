#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const bodyObj = JSON.parse(body);
    console.log(bodyObj.title);
  }
});
