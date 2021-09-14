#!/usr/bin/node

/* Write a script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    const body = JSON.parse(response.body);
    console.log(body.title);
  }
});
