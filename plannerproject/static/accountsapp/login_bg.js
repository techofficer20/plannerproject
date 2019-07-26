const body = document.querySelector(".login_body");

const IMG_NUMBER = 1;
function handleImgLoad() {}
function paintImage(imgNumber) {
  const image = new Image();
  image.src ="http://"+location.host +`/static/accountsapp/images/${imgNumber}.jpg`;
  image.classList.add("bgImage");
  body.appendChild(image);
}
function init() {
  const number = IMG_NUMBER;
  paintImage(number);
}
init();