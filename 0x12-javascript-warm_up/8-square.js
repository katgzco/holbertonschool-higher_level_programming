#!/usr/bin/node
import { argv } from 'process';
const FIRST_ARGUMENT = argv[2];
const PARSE_INT_RESULT = parseInt(FIRST_ARGUMENT);;
let column = 0;

if (isNaN(PARSE_INT_RESULT)) {
  console.log('Missing size');
} else {
  while (column < PARSE_INT_RESULT) {
    console.log('x'.repeat(PARSE_INT_RESULT));
    column++;
  }
}
