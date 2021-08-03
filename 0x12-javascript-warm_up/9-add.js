#!/usr/bin/node
import { argv } from 'process';

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(argv[2], argv[3]);
