#!/usr/bin/node
const firstargument = process.argv;

if (firstargument === undefined) {
  console.log('No argument');
} else {
  console.log(firstargument);
}