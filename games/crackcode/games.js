const difam = 22;
const difnuml = Math.floor(Math.random() * difam) + 3;
const difnumr = Math.floor(Math.random() * difam) + 3;

const num = Math.floor(Math.random() * 9999) + 1;
const up = num + difnuml
const down = num - difnumr
const between = `The number is between ${down} and ${up}`

// the random number
console.log(`${up} : ${down}`);

let outputext = 'hello';


// selecting the html
const number = document.querySelector('#number');
const myForm = document.querySelector('#my-form');
const res = document.querySelector('.output');
let guess = document.querySelector('.btnn');
let outputText = document.querySelector(outputext);
const dev = document.createTextNode(between);
const linkText = document.createTextNode(`${num} . . . . . `);

// ------------------------------------------------------------------------------------------------------------------------------------

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
  e.preventDefault();

  while (guess != num) {
    if (guess.value == num) {
      res.innerHTML = 'Well done you won :)';
      break

    }else if (guess.value !== num) {
      res.innerHTML = 'Inncorect try again';
      setTimeout(() => res.innerHTML = '', 3000);
      guess.value = '';
      break

    }else {
      console.log('hi');
      break
    }
  }
}


// ------------------------------------------------------------------------------------------------------------------------------------

// transforming the text
const a = document.createElement('h3');
const out = document.createElement('h3');
if (false) {a.appendChild(linkText);}

a.appendChild(dev);
number.appendChild(a);

console.log(difam);
