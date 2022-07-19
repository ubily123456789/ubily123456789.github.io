const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('.users');
const linkText = document.createTextNode("dev");


myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
  e.preventDefault();

  if (nameInput.value === 'ReAsEaRcH StYdY') {
    const a = document.createElement('a');
    a.appendChild(linkText);
    a.href = "dev.html";

    userList.appendChild(a);
    userList.classList.add('ull');
    a.classList.add('lnk');
  }

  // testing

  if (nameInput.value === 'testing') {
    alert('nothing for testing right now');
  }
}
