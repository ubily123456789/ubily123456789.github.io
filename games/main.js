const num = Math.floor(Math.random() * 99) + 1;

const number = document.querySelector('#number');
const myForm = document.querySelector('#my-form');
const res = document.querySelector('.output');
let guess = document.querySelector('.btnn');
const linkText = document.createTextNode(`dev: ${num}`);

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
  e.preventDefault();

  if (guess.value == num) {
    console.log('hi');
  }else{
    console.log('hello');
  }


  console.log('hi');
}


if (true) {number.appendChild(linkText)}
