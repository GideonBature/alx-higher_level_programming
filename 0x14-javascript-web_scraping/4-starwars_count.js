#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.
const process = require('process');
const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonBody = JSON.parse(body);
    const movies = jsonBody.results;
    const mainCharacter = movies.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    const len = mainCharacter.length;
    console.log(len);
  }
});
