const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');
const linkText = document.createTextNode("Iceland");


myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'Google') {
        alert('you clicked me :)');
    }

    // testing

    if (nameInput.value === 'testing') {
        alert('nothing for testing right now');
    }
}
