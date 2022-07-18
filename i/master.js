const myForm = document.querySelector('#my-form');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    alert('hello');
}
