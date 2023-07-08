#!/usr/bin/node
const firstargument = process.argv[2];

if (firstargument === undefined) {
  console.log('No argument');
} else {
  console.log(firstargument);
}