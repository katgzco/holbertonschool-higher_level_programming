#!/usr/bin/node
const FIRST_ARGUMENT = process.argv[2];
const PARSE_INT_RESULT = parseInt(FIRST_ARGUMENT);
let valueParseIntResult;

if (isNaN(PARSE_INT_RESULT)) {
  valueParseIntResult = 'Not a number';
} else {
  valueParseIntResult = `My number: ${PARSE_INT_RESULT}`;
}
console.log(valueParseIntResult);
