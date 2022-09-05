var charecter = document.querySelector('#charecter')
var block = document.querySelector('#block')

function jump() {
  charecter.classList.add('animate')
  setTimeout(function(){
    charecter.classList.remove('animate')
  },500)
}
