import copy
import math
from import9 import chaine

#Je me suis compliquer la taches mais je me garde dans cette voie car cest un entrenement algo 
#normalement pas besoin de avoir la liste des toute les possibiliter


#au bout de 3 heure ou je bloque je vais utilise cette fonction
from itertools import permutations


listinstruction = chaine.splitlines()
chaine2 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

# chaine = chaine2
# listinstruction = chaine2.splitlines()

def getListDesVilles(listinstruction):
    listeDesVilles = []
    #print(chaine.split())
    for instruction in listinstruction:
        instructionSpliter = instruction.split()
        if instructionSpliter[0] not in listeDesVilles:
            listeDesVilles.append(instructionSpliter[0])
        if instructionSpliter[2] not in listeDesVilles:
            listeDesVilles.append(instructionSpliter[2])
    return listeDesVilles
    

def createAllPath(chaine):
    listeDesVilles = getListDesVilles(listinstruction)
    #print(list(permutations(listeDesVilles)))
    return list(permutations(listeDesVilles))


    
listeDesChemin = createAllPath(listinstruction)

listeDistance = []
for chemin in listeDesChemin:
    compteur = 0
    for i in range(len(chemin)-1):
        anciencompt = copy.copy(compteur)
        compteurboucle = 0 # je sais que cest pas comme ca mais trop de truc a changer
        for instruction in listinstruction:
            #print(chemin)
            #print(instruction)
            instructionSpliter = instruction.split()
            if instructionSpliter[0] == chemin[i] and instructionSpliter[2] == chemin [i+1]:
                compteur += float(instructionSpliter[4])
            
            #print(compteur)
            #print(anciencompt)
            if anciencompt == compteur and compteurboucle == len(listinstruction)-1 :
                compteur = math.inf
            #print(compteur)
            compteurboucle += 1
    listeDistance.append(compteur)

print(listeDistance)
print(min(listeDistance))
#print(listeDesChemin)

# lalgo est faux
# le probleme est plus dur que je pensais car on peut faire demi tour aller dans la meme ville donc 
# il va vraiment falloir utiliser un algorithme de tu plus court chemin et encore je pense quil le faudra
# modifier lago en question