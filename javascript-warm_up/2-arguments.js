#!/usr/bin/node
const ArgumentsNum = process.argv.length - 2;
if (ArgumentsNum === 0) {
  console.log('No argument');
} else if (ArgumentsNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
