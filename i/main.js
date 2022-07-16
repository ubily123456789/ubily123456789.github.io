const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');
const linkText = document.createTextNode("Iceland");


myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'google') {
        alert('you clicked me');
    }

    // testing

    if (nameInput.value === 'testing') {
        const a = document.createElement('a');
        a.appendChild(linkText);
        a.href = "https://ubily123456789.github.io/i/iceland.html";
        userList.appendChild(a);
        userList.classList.add('ull');
        a.classList.add('lnk');
    }
}
