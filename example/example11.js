const read = require("./read");

let n = read.read_int();

let j = (5 * 10 + (n - 5)) / 10;
let sum = 0;

console.log(j)

for (let i = 0; i < 5; i = i + 1) {
  sum = n + j
  console.log("Sum:", sum)
}