var charecter = document.querySelector('#charecter')
var block = document.querySelector('#block')
var ret = document.querySelector('.retry')

let score = 0

function jump() {
  charecter.classList.add('animate')
  setTimeout(function(){
    charecter.classList.remove('animate')
  },500)
}

function retry() {
  window.location = "crackcode/../index.html"
}

var checkDead = setInterval(function() {
  let characterTop = parseInt(window.getComputedStyle(charecter).getPropertyValue("top"));
  let blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
  if (blockLeft<20 && blockLeft>-20 && characterTop>=130) {
    block.style.animation = "none";
    alert(`you lost your score: ${Math.floor(score/100)}`)
  } else {
    score ++;
  }
}, 10)
