#!/usr/bin/node
import { argv } from 'process';
const FIRST_ARGUMENT = argv[2];
const SECOND_ARGUMENT = argv[3];

console.log(`${FIRST_ARGUMENT} is ${SECOND_ARGUMENT}`);
