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

function srcheachXmax(arrayInputLetter,indexLigne,indexCol,letterIndex){
    if (arrayInputLetter == "X") {
        
    }
}

function colorToGreen(ligne,colonne){
    let selector = `.l${ligne} > .c${colonne}`;
    let elementEnTraitement = document.querySelector(selector);
    elementEnTraitement.style.color = "green";
}

const Xmas = "XMAS"
function verifAll(arrayInputLetter,indexLigne,indexCol){
    let arrayXmas = []
    if(isInRange(indexLigne,indexCol,arrayInputLetter.length,arrayInputLetter[0].length) ){
        if(arrayInputLetter[indexLigne][indexCol] != Xmas[0]){
            return arrayXmas
        }
    }
    //pas opti mais le code est simplifier
    if (verifColBas(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("CB");
    if (verifColHaut(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("CH");
    if (verifDiaBasDer(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("DBD");
    if (verifDiaBasDevant(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("DBV");
    if (verifDiaHautDer(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("DHR");
    if (verifDiaHautDevant(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("DHV");
    if (verifLigneDer(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("LDR");
    if (verifLigneDevant(arrayInputLetter,indexLigne,indexCol)) arrayXmas.push("LDV");
    return arrayXmas
}
function verifLigneDevant(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
    }
    for (let i = 0; i < 4; i++) {
        let ligne = indexLigne;
        let colonne = indexCol + i;
        colorToGreen(ligne,colonne)
    }
    
    return true
}
function verifLigneDer(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }

    }
    for (let i = 0; i < 4; i++) {
        let ligne = indexLigne;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne)
    }
    
    return true
}
function verifDiaHautDevant(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }
    for (let i = 0; i < 4; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne)
    }
    return true
}
function verifDiaBasDevant(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }
    for (let i = 0; i < 4; i++) {
        
        let ligne = indexLigne + i;
        let colonne = indexCol + i;
        colorToGreen(ligne,colonne)
    }
    return true
}
function verifDiaBasDer(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne - i;
        let colonne = indexCol + i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }
    for (let i = 0; i < 4; i++) {
        
        let ligne = indexLigne - i;
        let colonne = indexCol + i;
        colorToGreen(ligne,colonne)
    }
    return true
}
function verifDiaHautDer(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne - i;
        let colonne = indexCol - i;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }
    for (let i = 0; i < 4; i++) {
        
        let ligne = indexLigne - i;
        let colonne = indexCol - i;
        colorToGreen(ligne,colonne)
    }
    return true
}
function verifColHaut(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne - i;
        let colonne = indexCol;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }    
    for (let i = 0; i < 4; i++) {
        let ligne = indexLigne - i;
        let colonne = indexCol;
        colorToGreen(ligne,colonne)
    }
    return true
}
function verifColBas(arrayInputLetter,indexLigne,indexCol){
    for (let i = 1; i < 4; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol;
        if(!isInRange(ligne,colonne,arrayInputLetter.length,arrayInputLetter[0].length)){
            return false
        }
        if(arrayInputLetter[ligne][colonne] != Xmas[i]){
            return false
        }
        
    }
    for (let i = 0; i < 4; i++) {
        let ligne = indexLigne + i;
        let colonne = indexCol;
        colorToGreen(ligne,colonne)
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
            await delay(300);

            
            tableXmas = verifAll(arrayInputLetter,indexLigne,indexCol);
            //console.log(tableXmas)
            compteur += tableXmas.length;
            console.log(elementEnTraitementWasGreen)
            
            elementEnTraitement.style.color = `${elementEnTraitementWasGreen || elementEnTraitement.style.color == "green"  ? "green" : "grey"} `;
        }
    }
    console.log(compteur);
}

Resolution(input);
