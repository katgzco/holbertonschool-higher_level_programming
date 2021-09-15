#!/usr/bin/node

/* Write a script that gets the contents of a
webpage and stores it in a file. */

const url = process.argv[2];
const file = process.argv[3];

const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
