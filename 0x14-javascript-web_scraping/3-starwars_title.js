#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const process = require('process');
const request = require('request');

const id = process.argv[2];
const path = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(path, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(body.title);
  }
});
