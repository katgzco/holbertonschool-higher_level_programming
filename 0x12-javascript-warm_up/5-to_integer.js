#!/usr/bin/node
import { argv } from 'process';
const FIRST_ARGUMENT = argv[2];
const PARSE_INT_RESULT= parseInt(FIRST_ARGUMENT);
let valueParseIntResult;

if (isNaN(PARSE_INT_RESULT)) {
  valueParseIntResult = 'Not a number';
} else {
  valueParseIntResult = `My number: ${PARSE_INT_RESULT}`;
}
console.log(valueParseIntResult);
