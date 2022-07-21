const difam = 10; // going to be input
const difnuml = Math.floor(Math.random() * difam) + 3;
const difnumr = Math.floor(Math.random() * difam) + 3;

const num = Math.floor(Math.random() * 9999) + 1;
const up = num + difnuml
const down = num - difnumr
const between = `The number is between ${up} and ${down}`

// the random number
console.log(`${up} : ${down}`);


// selecting the html
const number = document.querySelector('#number');
const userList = document.querySelector('#myForm');
const myForm = document.querySelector('#my-form');
let guess = document.querySelector('.btnn');
const dev = document.createTextNode(between);
const linkText = document.createTextNode(`${num} . . . . . `);

// ------------------------------------------------------------------------------------------------------------------------------------

myForm.addEventListener('submit', onSubmit);


function onSubmit(e) {
  e.preventDefault();


  if (guess.value == num) {
    console.log('hi');
  }else if (guess.value !== num) {
    console.log(guess.value);
    guess.value = '0';
  }else {
    console.log('hi');
  }
}


// ------------------------------------------------------------------------------------------------------------------------------------

// transforming the text
const a = document.createElement('h3');
a.appendChild(linkText);
a.appendChild(dev);

number.appendChild(a);
