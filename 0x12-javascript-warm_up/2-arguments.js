#!/usr/bin/node
let argumentStatus;
if (process.argv.length === 2) {
  argumentStatus = 'No argument';
} else if (process.argv.length === 3){
  argumentStatus = 'Argument found';
} else {
  argumentStatus = 'Arguments found';
}
console.log(argumentStatus);
