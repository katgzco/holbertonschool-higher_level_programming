#!/usr/bin/node

/* Write a script that prints the number of movies
where the character “Wedge Antilles” is present. */

let counter = 0;
const url = process.argv[2];
const request = require('request');

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    const body = JSON.parse(response.body);
    const films = body.results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('/18/')) { counter++; }
      }
    }
    console.log(counter);
    }
});
