const num = Math.floor(Math.random() * 99) + 1;
const number = document.querySelector('#number');
const myForm = document.querySelector('#my-form');
const res = document.querySelector('.output');
const guess = document.querySelector('.btnn');
const linkText = document.createTextNode(`dev: ${num}`);


function doCalc() {
  if (guess.value > num) {
    res.innerHTML = 'too high';
    setTimeout(() => res.innerHTML = '', 3000);
    guess.value = '';

  } else if (guess.value == num) {
    console.log(('b' + 'a' + + 'a' + 'a').toLowerCase()); // if you see this feel happy and go to this vidio https://www.youtube.com/watch?v=sRWE5tnaxlI its were i learned it from go check it out :)
    res.innerHTML = 'Just right :)';

  } else {
    res.innerHTML = 'too low';
    setTimeout(() => res.innerHTML = '', 3000);
    guess.value = '';
  }
}


myForm.addEventListener('submit', onSubmit);
function onSubmit(e) {e.preventDefault();doCalc();}
if (false) {number.appendChild(linkText)}
