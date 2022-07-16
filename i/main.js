const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');


myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'google') {
        alert('you clicked me');
    }

    // testing

    if (nameInput.value === 'testing') {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value}`));

        userList.appendChild(li);
    }

}
