function remove1() {
  let count = document.querySelector("#request-num").innerText;
  count--;
  document.querySelector("#request-num").innerText = `${count}`;
  document.querySelector("#todd").remove();
}
function remove2() {
  let count = document.querySelector("#request-num").innerText;
  count--;
  document.querySelector("#request-num").innerText = `${count}`;
  document.querySelector("#phil").remove();
}
function add() {
  let count = document.querySelector("#connection-num").innerText;
  count++;
  document.querySelector("#connection-num").innerText = `${count}`;
}