from import3 import chaine

instructions = chaine.splitlines()

compteurDePossible = 0
for i in instructions:
    chiffres = sorted(list(map(int, i.split())))
    #print(chiffres)
    if ( int(chiffres[0]) + int(chiffres[1]) ) > int(chiffres[2]):
        compteurDePossible += 1
print(compteurDePossible)

##862