#!/usr/bin/node
const args = process.argv;
if (args.length > 2) {
  args[2] = parseInt(args[2], 10);
  if (isNaN(args[2])) {
    console.log('Not a number');
  } else {
    console.log('My number:', args[2]);
  }
} else {
  console.log('Not a number');
}
