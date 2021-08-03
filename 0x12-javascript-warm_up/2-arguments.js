#!/usr/bin/node
import { argv } from 'process';

let argumentStatus;

if (argv.length === 2) {
  argumentStatus = 'No argument';
} else if (argv.length === 3){
  argumentStatus = 'Argument found';
} else{
  argumentStatus = 'Arguments found';
}
console.log(argumentStatus);
