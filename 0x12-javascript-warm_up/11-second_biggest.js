#!/usr/bin/node
import { argv } from 'process';
const arrayForSort = [];
let i;
if (argv.length <= 3) {
  console.log(0);
} else {
  for (i in argv) {
    arrayForSort.push(parseInt(argv[i]));
  }
  arrayForSort.sort(function (a, b) { return a - b; });
  console.log(arrayForSort[i - 1]);
}
