let high1 = document.querySelector("#high-num1");
    let high2 = document.querySelector("#high-num2");
    let high3 = document.querySelector("#high-num3");
    let high4 = document.querySelector("#high-num4");
    let low1 = document.querySelector("#low-num1");
    let low2 = document.querySelector("#low-num2");
    let low3 = document.querySelector("#low-num3");
    let low4 = document.querySelector("#low-num4");

function temp() {
  let degrees = document.querySelector("#degrees").value;
  console.log(degrees);
  if (degrees === "f") {
    high1.innerText = "75";
    high2.innerText = "80";
    high3.innerText = "69";
    high4.innerText = "78";
    low1.innerText = "65";
    low2.innerText = "66";
    low3.innerText = "61";
    low4.innerText = "70";
  } else if (degrees === "c") {
    high1.innerText = "24";
    high2.innerText = "27";
    high3.innerText = "21";
    high4.innerText = "26";
    low1.innerText = "18";
    low2.innerText = "19";
    low3.innerText = "16";
    low4.innerText = "21";
  }
}

// let change1 = document.querySelector("#high-num1").innerText;
// console.log(change1)

function alertUser() {
  alert("Loading weather report...");
}

function remove() {
  document.querySelector("#cookies").remove();
}