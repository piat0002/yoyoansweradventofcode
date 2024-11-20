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