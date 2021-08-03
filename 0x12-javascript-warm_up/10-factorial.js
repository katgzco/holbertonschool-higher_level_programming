#!/usr/bin/node
import { argv } from 'process';
function factorial (number) {
  if (isNaN(number) || number === 0 || number === 1) { return 1; } else { return (number * factorial(number - 1)); }
}

console.log(factorial(argv[2]));
