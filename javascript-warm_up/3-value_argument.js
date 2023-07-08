#!/usr/bin/node
const fargument = process.argv[2];

if (fargument === undefined) {
  console.log('No argument');
} else {
  console.log(fargument);
}