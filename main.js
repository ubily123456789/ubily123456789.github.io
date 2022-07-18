const nameInput = document.querySelector('.dev');
const myForm = document.querySelector('.sub');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'google') {
        alert('hello')
    }
}
