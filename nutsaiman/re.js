let re = document.getElementById('ree')

const searchParams = new URLSearchParams(window.location.search);
let gift = searchParams.get('bckptxt')

if (searchParams.has('args') && searchParams.get('bckptxt')) {

    let ham = '';

    if (gift.includes("the")) {console.log("lkjuxb "); gift = gift.replace("the", "¦")}
    if (gift.includes("this")) {console.log("lkjuxb "); gift = gift.replace("this", "`")}
    if (gift.includes("and")) {console.log("lkjuxb "); gift = gift.replace("and", "¬")}
    if (gift.includes("frog")) {console.log("lkjuxb "); gift = gift.replace("frog", "|")}


    for (let i = 0; i < gift.length; i++) {
        const letter = gift[i];
        
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

    re.innerHTML = ham

}
