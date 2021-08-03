#!/usr/bin/node
const arrayForSort = [];
let i;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i in process.argv) {
    arrayForSort.push(parseInt(process.argv[i]));
  }
  arrayForSort.sort(function (a, b) { return a - b; });
  console.log(arrayForSort[i - 1]);
}
