const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('.dev');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'google') {
        alert('hello')
    }
}
