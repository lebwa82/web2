"use strict"

console.log("123123");
const element = document.querySelector('button')

element.addEventListener('click', function (event) {
  console.log('По клику добавляю картинку', event.type)
  const image = document.createElement('img');
  image.src  = 'picture.jpg';
  document.body.appendChild(image);
});

