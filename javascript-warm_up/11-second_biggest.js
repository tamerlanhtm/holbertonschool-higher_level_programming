#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  args.splice(args.indexOf(max), 1);
  console.log(Math.max(...args));
}
