#!/usr/bin/node
const num = process.argv[2];
const phrase = 'C is fun';

if (num) {
  for (let i = 0; i < num; i++) {
    console.log(phrase);
  }
} else {
  console.log('Missing number of occurrences');
}
