#!/usr/bin/node
const args = process.argv;
if (args.length > 2) {
  const number = parseInt(args[2], 10);
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
  if (isNaN(number)) {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
