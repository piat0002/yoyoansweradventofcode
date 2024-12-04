var input2 = `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`;

input = input2

//creation de linterface 
container = document.querySelector(".container");
var table = document.createElement("table");
var tbody = document.createElement("tbody");

let arrayInput = input.split(/\r?\n|\r|\n/g);

arrayInput.forEach((ligne,indexLigne) => {
    var tr = document.createElement("tr");
    tr.classList.add("l" + indexLigne);
    arrayLetter = ligne.split('');
    arrayLetter.forEach((element,index) => {
        tr.innerHTML += `<td class="c${index}">${element}</td>`;
    });
    tbody.appendChild(tr);
});
table.appendChild(tbody);

container.appendChild(table);



// resolution du probleme

function createArrayInputLetter(input){
    let arrayInput = input.split(/\r?\n|\r|\n/g);
    arrayInput.forEach((element,index) => {
        arrayInput[index] = element.split('');
    });
    return arrayInput;
}
const delay = ms => new Promise(res => setTimeout(res, ms));

function isInRange(indexLigne,indexCol,arrayInputlength,ligneLength){
    return indexLigne < 0 & indexLigne < 0 & indexLigne < arrayInputlength && indexCol < ligneLength;
}

function srcheachXmax(arrayInputLetter,indexLigne,indexCol){
    if (arrayInputLetter == "X") {
        
    }
}
verifAll(arrayInputLetter,indexLigne,indexCol){
    let = count
    let arrayXmas = []
    verifColBas(arrayInputLetter,indexLigne,indexCol)
    verifColHaut(arrayInputLetter,indexLigne,indexCol)
    verifDiaBasDer(arrayInputLetter,indexLigne,indexCol)
    verifDiaBasDevant(arrayInputLetter,indexLigne,indexCol)
    verifDiaHautDer(arrayInputLetter,indexLigne,indexCol)
    verifDiaHautDevant(arrayInputLetter,indexLigne,indexCol)
    verifLigneDer(arrayInputLetter,indexLigne,indexCol)
    verifLigneDevant(arrayInputLetter,indexLigne,indexCol)
    return [,count]
}
function verifLigneDevant(arrayInputLetter,indexLigne,indexCol){
}
function verifLigneDer(arrayInputLetter,indexLigne,indexCol){

}
function verifDiaHautDevant(arrayInputLetter,indexLigne,indexCol){

}
function verifDiaBasDevant(arrayInputLetter,indexLigne,indexCol){

}
function verifDiaBasDer(arrayInputLetter,indexLigne,indexCol){

}
function verifDiaHautDer(arrayInputLetter,indexLigne,indexCol){

}
function verifColHaut(arrayInputLetter,indexLigne,indexCol){

}
function verifColBas(arrayInputLetter,indexLigne,indexCol){

}
async function Resolution(input){
    let compteur = 0; 
    let arrayInput = input.split(/\r?\n|\r|\n/g);
    let arrayInputlength = arrayInput.length;
    let ligneLength = arrayInput.length;
    let arrayInputLetter = createArrayInputLetter(input);
    //console.log(arrayInputLetter)
    for (let indexLigne = 0; indexLigne < arrayInputlength; indexLigne++) {
        for (let indexCol = 0; indexCol < ligneLength; indexCol++) {
            let selector = `.l${indexLigne} > .c${indexCol}`;
            let elementEnTraitement = document.querySelector(selector);
            elementEnTraitement.style.color = 'blue';
            arrayInputLetter[indexLigne][indexCol]
            await delay(500);

            elementEnTraitement.style.color = `${elementEnTraitement.style.color == "green" ? "green" : "grey"} `;
        }
    }
    console.log(compteur);
}

Resolution(input);
