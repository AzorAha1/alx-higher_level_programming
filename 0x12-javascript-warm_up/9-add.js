#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}
if (args.length > 2) {
  const result = add(args[2], args[3]);
  console.log(result);
}
else
{
    console.log(NaN);
}