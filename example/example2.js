let array = [5, 10, 2, 3, 4, 12, 1, 54];
let min = 0;

for (let i = 0; i < array.length - 1; i += 1) {
  if (array[i] > array[i+1]) 
    min = array[i+1];
}