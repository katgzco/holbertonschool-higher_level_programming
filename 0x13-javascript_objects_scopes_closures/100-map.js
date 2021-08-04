#!/usr/bin/node
const listToCompute = require('./100-data').list;
const arrayComputed = listToCompute.map((x, i) => x * i);
console.log(listToCompute);
console.log(arrayComputed);
