#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length > 1) {
  const sorted = args.map(Number).sort(function (a, b) { return parseInt(b, 10) - parseInt(a, 10); });
  console.log(sorted[1]);
} else {
  console.log(0);
}
