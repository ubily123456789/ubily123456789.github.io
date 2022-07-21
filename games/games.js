const difam = 10; // going to be input
const difnum = Math.floor(Math.random() * difam) + 1;

const num = Math.floor(Math.random() * 9999) + 1;
const up = num + difnum
const down = num - difnum

const between = `The number is between ${up} and ${down}`

// the random number
console.log(`${up} : ${down}`);


// selecting the html
const number = document.querySelector('#number');
const userList = document.querySelector('#myForm');
const myForm = document.querySelector('#my-form');
const guess = document.querySelector('.btnn');
const dev = document.createTextNode(between)
const linkText = document.createTextNode(`${num} . . . . . `);

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
a.appendChild(dev);

number.appendChild(a);
