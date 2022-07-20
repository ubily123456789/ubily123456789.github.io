const difam = 10; // going to be input
const difnum = Math.floor(Math.random() * difam) + 1;

// the random number

const num = Math.floor(Math.random() * 9999) + 1;

const up = num + difnum
const down = num - difnum
console.log(`${up} : ${down}`);

// selecting the html
const number = document.querySelector('#number');
const userList = document.querySelector('#myForm');
const myForm = document.querySelector('#my-form');
const guess = document.querySelector('.btnn');
const linkText = document.createTextNode(num);

// ------------------------------------------------------------------------------------------------------------------------------------

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    console.log(guess.value);
}


// ------------------------------------------------------------------------------------------------------------------------------------

// transforming the text
const a = document.createElement('h3');
a.appendChild(linkText);

number.appendChild(a);
