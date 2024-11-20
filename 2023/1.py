from import1 import chaine
chaine2 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
listinstruction = chaine.splitlines()
#listinstruction = chaine2.splitlines()

def isAdigit(letter):
    # il y a pas de 0 car cest pas dans la liste

    listeDesNombres = "123456789"     
    for digit in listeDesNombres:
        if letter == digit:
            return True
    return False



count = 0
for ligne in listinstruction:
    first = 0
    last = 0
    for letter in ligne:
        if isAdigit(letter):
            last = letter
            if first == 0:
                first = letter
    count += int(first+last) # first et last sont bien des chaines de caractere donc cest une concatenation pas de piege normalement

print(count)
    
            
## part 2

chaine3 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

#listinstruction = chaine3.splitlines()
count = 0
for ligne in listinstruction:
    first = 0
    last = 0
    compteur = 0
    for letter in ligne:
        
        if letter == "o":
            if ligne[compteur + 1 : compteur + 2+1] == "ne":
                letter = "1"
        elif letter == "t":
            #print(ligne[compteur + 1 : compteur + 2+1])
            if ligne[compteur + 1 : compteur + 2+1] == "wo":
                #print("ok")
                letter = "2"
            if ligne[compteur + 1 : compteur + 4+1] == "hree":
                letter = "3"
        elif letter == "f":
            if ligne[compteur + 1 : compteur + 3+1] == "our":
                letter = "4"
            if ligne[compteur + 1 : compteur + 3+1] == "ive":
                letter = "5"
        elif letter == "s":
            if ligne[compteur + 1 : compteur + 2+1] == "ix":
                letter = "6"
            if ligne[compteur + 1 : compteur + 4+1] == "even":
                letter = "7"
        elif letter ==  "e": 
            if ligne[compteur + 1 : compteur + 4+1] == "ight":
                letter = "8"
        elif letter ==  "n": 
            if ligne[compteur + 1 : compteur + 3+1] == "ine":
                letter = "9"


        if isAdigit(letter):
            last = letter
            if first == 0:
                first = letter
        
        
        compteur += 1
    #print(first+last)
    count += int(first+last) # first et last sont bien des chaines de caractere donc cest une concatenation pas de piege normalement

print(count)