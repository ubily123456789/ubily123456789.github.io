const difam = 10; // going to be input
const difnum = Math.floor(Math.random() * difam) + 1;

// the random number

const num = Math.floor(Math.random() * 9999) + 1;

const up = num + difnum
const down = num - difnum
console.log(`${up} : ${down}`);

// selecting the html
const number = document.querySelector('#number');
const linkText = document.createTextNode(num);

// ------------------------------------------------------------------------------------------------------------------------------------





// ------------------------------------------------------------------------------------------------------------------------------------

// transforming the text
const a = document.createElement('h3');
a.appendChild(linkText);

number.appendChild(a);
