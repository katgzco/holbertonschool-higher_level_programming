#!/usr/bin/node
const FIRST_ARGUMENT = process.argv[2];
const PARSE_INT_RESULT = parseInt(FIRST_ARGUMENT);
let column = 0;

if (isNaN(PARSE_INT_RESULT) && PARSE_INT_RESULT > 0) {
  console.log('Missing size');
} else {
  while (column < PARSE_INT_RESULT) {
    console.log('x'.repeat(PARSE_INT_RESULT));
    column++;
  }
}
