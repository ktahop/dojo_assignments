// Pring odds 1-20
for (var i = 1; i < 21; i++) {
  if (i%2 !== 0) {
    console.log(i);
  }
}

console.log(" "); // Used to seperate results in output

// Decreasing Multiples of 3
for (var j = 100; j > -1; j--) {
  if (j%3 == 0) {
    console.log(j)
  }
}

console.log(" "); // Used to seperate results in output

// Pring the sequence
var k = 6
var sequence = 4;
while (k > 0) {
  console.log(sequence);
  sequence -= 1.5;
  k--;
}

console.log(" "); // Used to seperate results in output

// Sigma
var sum = 0
for (var l = 1; l <= 100; l++) {
  sum += l;
}
console.log(sum);

console.log(" "); // Used to seperate results in output

// Factorial
var product = 1;
for (var m = 1; m <= 12; m++) {
  product *= m;
}
console.log(product);

console.log(" "); // Used to seperate results output