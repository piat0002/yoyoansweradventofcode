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
    return indexLigne >= 0 && indexCol >= 0 && indexLigne < arrayInputlength && indexCol < ligneLength;
}

function colorToGreen(ligne,colonne){
    let selector = `.l${ligne} > .c${colonne}`;
    let elementEnTraitement = document.querySelector(selector);
    elementEnTraitement.style.color = "green";
}

const mas = "MAS"
const sam = "SAM"
function verifAll(arrayInputLetter,indexLigne,indexCol){
    let arrayXmas = []
    if(isInRange(indexLigne,indexCol,arrayInputLetter.length,arrayInputLetter[0].length) ){
        if(arrayInputLetter[indexLigne][indexCol] != mas[1]){
            return arrayXmas
        }
    }
    if (IsXMAS1(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("XMAS1");
    if (IsXSAM1(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("XSAM1");
    if (IsXMAS2(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("XMAS2");
    if (IsXSAM2(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("XSAM2");
    return arrayXmas
}

function IsXMAS1(arrayInputLetter,indexLigne,indexCol){
    //mas
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != mas[i+1]){
            return false
        }
    }
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != mas[i+1]){
            return false
        }
        
    }

    //color green si tous est bon
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne);

        ligne = indexLigne + i;
        colonne = indexCol + i;
        colorToGreen(ligne,colonne);
    }
    return true
}
function IsXMAS2(arrayInputLetter,indexLigne,indexCol){
    //mas
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != mas[i+1]){
            return false
        }
    }
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != sam[i+1]){
            return false
        }
        
    }

    //color green si tous est bon
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne);

        ligne = indexLigne + i;
        colonne = indexCol + i;
        colorToGreen(ligne,colonne);
    }
    return true
}
function IsXSAM1(arrayInputLetter,indexLigne,indexCol){
    //sam
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != sam[i+1]){
            return false
        }
    }
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != sam[i+1]){
            return false
        }
        
    }
    //color green si tous est bon
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne);

        ligne = indexLigne + i;
        colonne = indexCol + i;
        colorToGreen(ligne,colonne);
    }
    return true
}
function IsXSAM2(arrayInputLetter,indexLigne,indexCol){
    //sam
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != sam[i+1]){
            return false
        }
    }
    //diago bas devant
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != mas[i+1]){
            return false
        }
        
    }
    //color green si tous est bon
    for (let i = -1; i < 2; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne);

        ligne = indexLigne + i;
        colonne = indexCol + i;
        colorToGreen(ligne,colonne);
    }
    return true
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
            let elementEnTraitementWasGreen = elementEnTraitement.style.color == "green"
            elementEnTraitement.style.color = `${"blue"} `;
            arrayInputLetter[indexLigne][indexCol]
            await delay(100);

            
            tableXmas = verifAll(arrayInputLetter,indexLigne,indexCol);
            console.log(tableXmas)
            compteur += tableXmas.length;
            
            elementEnTraitement.style.color = `${elementEnTraitementWasGreen || elementEnTraitement.style.color == "green"  ? "green" : "grey"} `;
        }
    }
    console.log(compteur);
}

Resolution(input);