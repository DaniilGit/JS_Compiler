let a = 15;
let b = 18;

while (a && b)
  b < a ? a %= b : b %= a;
  
console.log(a | b);