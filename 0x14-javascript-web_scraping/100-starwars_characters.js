#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const process = require('process');
const request = require('request');

const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const charUrl of characters) {
      request(charUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    }
  }
});
