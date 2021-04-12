const str = "Hello World!";
let n = 1000;

while (n < 1000 - 1) {
  console.log(str.includes("World"));
  n += 1;
}