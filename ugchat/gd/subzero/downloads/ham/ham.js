// ima "borrow some code 🤣"
const customMapping = {
    'a': '430',
    'b': '921',
    'c': '815',
    'd': '694',
    'e': '128',
    'f': '341',
    'g': '255',
    'h': '879',
    'i': '772',
    'j': '636',
    'k': '985',
    'l': '543',
    'm': '204',
    'n': '168',
    'o': '329',
    'p': '482',
    'q': '191',
    'r': '763',
    's': '362',
    't': '612',
    'u': '289',
    'v': '451',
    'w': '701',
    'x': '849',
    'y': '567',
    'z': '998',
    'A': '597',
    'B': '309',
    'C': '681',
    'D': '429',
    'E': '885',
    'F': '676',
    'G': '792',
    'H': '107',
    'I': '376',
    'J': '185',
    'K': '464',
    'L': '240',
    'M': '732',
    'N': '711',
    'O': '963',
    'P': '654',
    'Q': '802',
    'R': '520',
    'S': '276',
    'T': '444',
    'U': '586',
    'V': '503',
    'W': '915',
    'X': '407',
    'Y': '149',
    'Z': '222',
    ' ': '707',    // space
    ',': '936',    // comma
    '.': '764',    // period
    '/': '295',    // forward slash
    '#': '111',    // hash
    '\'': '869',   // single quote
    ';': '150',    // semicolon
    ']': '357',    // right square bracket
    '[': '479',    // left square bracket
    '0': '723',    // numbers 0-9
    '1': '908',
    '2': '219',
    '3': '555',
    '4': '512',
    '5': '666',
    '6': '398',
    '7': '647',
    '8': '267',
    '9': '179',
};
function imint(inputString) {
    let outputString = '';
    for (let i = 0; i < inputString.length; i++) {
        const character = inputString.charAt(i);
        const replacement = customMapping[character];
        outputString += replacement ? replacement : character;
    }
    return outputString;
}
