let count = 3;
let add = document.querySelector("#add");

function addLike() {
  count++;
  console.log(count);
  add.innerText = `${count} like(s)`;
}