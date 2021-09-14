#!/usr/bin/node

/* Write a script that writes a string to a file. */

const fs = require('fs');

const content = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, content, err => {
  if (err) {
    console.error(err);
  }
});
