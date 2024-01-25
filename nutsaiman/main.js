let inp = document.getElementById('inp');
const res = document.getElementById('result');
const pass = document.getElementById('passss');
const trans = document.getElementById('trans');
let pasw = document.getElementById('pasw');
let rizz = document.getElementById('rizz');


go.style.display = "none";
inp.style.display = "none";

function passs() {
    console.log(pasw);
    if (pasw.value == "Kenneth you like cheese") {
        pass.style.display = "none";
        go.style.display = "block";
        inp.style.display = "block";
    }
}

function jump() {
    let ham = '';
    let inpu = inp.value;
    
    if (inp.value.includes("the")) {console.log("lkjuxb "); inp.value = inp.value.replace("the", "¦")}
    if (inp.value.includes("this")) {console.log("lkjuxb "); inp.value = inp.value.replace("this", "`")}
    if (inp.value.includes("and")) {console.log("lkjuxb "); inp.value = inp.value.replace("and", "¬")}
    if (inp.value.includes("frog")) {console.log("lkjuxb "); inp.value = inp.value.replace("frog", "|")}
   

    for (let i = 0; i < inp.value.length; i++) {
        const letter = inp.value[i];
        
        if (letter == "a") {console.log("rayom"); ham = ham.concat('<img src="img/apple.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "b") {console.log("rayom"); ham = ham.concat('<img src="img/canadianssayzed.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "c") {console.log("rayom"); ham = ham.concat('<img src="img/funnym.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "d") {console.log("rayom"); ham = ham.concat('<img src="img/dog.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "e") {console.log("rayom"); ham = ham.concat('<img src="img/window.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "f") {console.log("rayom"); ham = ham.concat('<img src="img/frabn.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "g") {console.log("rayom"); ham = ham.concat('<img src="img/gilbert.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "h") {console.log("rayom"); ham = ham.concat('<img src="img/hilbert.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "i") {console.log("rayom"); ham = ham.concat('<img src="img/weirdkthingy.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "j") {console.log("rayom"); ham = ham.concat('<img src="img/joker.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "k") {console.log("rayom"); ham = ham.concat('<img src="img/itsapen.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "l") {console.log("rayom"); ham = ham.concat('<img src="img/singing.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "m") {console.log("rayom"); ham = ham.concat('<img src="img/man.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "n") {console.log("rayom"); ham = ham.concat('<img src="img/rayom.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "o") {console.log("rayom"); ham = ham.concat('<img src="img/orange.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "p") {console.log("rayom"); ham = ham.concat('<img src="img/pineapple.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "q") {console.log("rayom"); ham = ham.concat('<img src="img/quartz.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "r") {console.log("rayom"); ham = ham.concat('<img src="img/racoon.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "s") {console.log("rayom"); ham = ham.concat('<img src="img/soap.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "t") {console.log("rayom"); ham = ham.concat('<img src="img/table.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "u") {console.log("rayom"); ham = ham.concat('<img src="img/up.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "v") {console.log("rayom"); ham = ham.concat('<img src="img/x.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "w") {console.log("rayom"); ham = ham.concat('<img src="img/walking.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "x") {console.log("rayom"); ham = ham.concat('<img src="img/fence.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "y") {console.log("rayom"); ham = ham.concat('<img src="img/fish.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "z") {console.log("rayom"); ham = ham.concat('<img src="img/jupiter.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == " ") {console.log("rayom"); ham = ham.concat('<img src="img/space.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "¦") {console.log("rayom"); ham = ham.concat('<img src="img/the.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "`") {console.log("rayom"); ham = ham.concat('<img src="img/this.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "¬") {console.log("rayom"); ham = ham.concat('<img src="img/and.png" alt="Rayom" width="150" height="100"></img>')}
        if (letter == "|") {console.log("rayom"); ham = ham.concat('<img src="img/frog.png" alt="Rayom" width="150" height="100"></img>')}
        
    }

    res.innerHTML = ham
    go.style.display = "none";
    inp.style.display = "none";
    rizz.innerHTML = `<h1>You put "${inpu}" this is the translation</h1>`;

}
