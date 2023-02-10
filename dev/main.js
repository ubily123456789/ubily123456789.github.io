window.onload = {
  function jump(getpar) {
    let parameters = new URLSearchParams(window.location.search)
    return parameters.get(getpar)
  }
  const myForm = document.querySelector('#my-form');
  const nameInput = document.querySelector('#name');
  const emailInput = document.querySelector('#email');
  const msg = document.querySelector('.msg');
  const userList = document.querySelector('#users');


  myForm.addEventListener('submit', onSubmit);

  function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'Google') {
      window.location = getpar
    }

    // testing

    if (nameInput.value === 'testing') {
      alert('nothing for testing right now');
    }
  }
}