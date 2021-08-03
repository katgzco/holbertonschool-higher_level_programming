#!/usr/bin/node
import { argv } from 'process';
let argumentStatus;
let length = 0;
for (const i in argv) {
  length++;
}
argumentStatus = length === 2 ? 'No argument' : argv[2];
console.log(argumentStatus);
