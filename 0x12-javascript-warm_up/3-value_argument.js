#!/usr/bin/node
let argumentStatus;
let length = 0;
for (const i in process.argv) {
  length++;
}
argumentStatus = length === 2 ? 'No argument' : process.argv[2];
console.log(argumentStatus);
