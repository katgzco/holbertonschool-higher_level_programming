#!/usr/bin/node
const firstArgument = process.argv[2];
let parseIntResult;
let valueParseIntResult;

parseIntResult = parseInt(firstArgument);
if (isNaN(parseIntResult)) {
  valueParseIntResult = 'Missing number of occurrences';
  console.log(valueParseIntResult);
} else {
  valueParseIntResult = 'C is fun';
  while (parseIntResult > 0) {
    console.log(valueParseIntResult);
    parseIntResult--;
  }
}
