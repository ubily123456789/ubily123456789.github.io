const number = document.querySelector('#number');
const linkText = document.createTextNode(num);

var num = Math.floor(Math.random() * 9999) + 1;
console.log(num);

const a = document.createElement('h3');
a.appendChild(linkText);

number.appendChild(a);
