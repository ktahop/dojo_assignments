console.log("page loaded...");

function autoPlayOn(element) {
  element.play();
  element.muted = true;
  element.loop = true;
}

function autoPlayOff(element) {
  element.pause();
}