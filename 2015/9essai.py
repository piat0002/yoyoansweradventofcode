import copy
import math
from import9 import chaine

#Je me suis compliquer la taches mais je me garde dans cette voie car cest un entrenement algo


#au bout de 3 heure je utilise cette fonction
from itertools import permutations


listinstruction = chaine.splitlines()
chaine2 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

chaine = chaine2
listinstruction = chaine2.splitlines()

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
    nombreDesPossibles = math.factorial(len(listeDesVilles))
    nombreDesPossiblesPourUneVille = math.factorial(len(listeDesVilles)-1)
    ListesPathVille = []
    for i in range(len(listeDesVilles)):
        listOtherVille = range(len(listeDesVilles)).pop(i)
        for y in listOtherVille:
            ok = 0

    # for i in range(nombreDesPossibles):
    #     PathVille = []
    #     for y in nombreDesPossiblesPourUneVille:
    #         for j in range(len(listeDesVilles)-1):
    #             for e in range()
    #                 PathVille.append() 
            
    #             ListesPathVille.append(PathVille)




def createAllPathForOneCity(listeDesVilles):
    ListPathForOneCity = []
    #calcul du nom de possibilite
    # nombreDesPossibles = 0
    # # si cest est on multipli ca marche pas du coup je commence le calcule comme ca
    # nombreDesPossibles = len(listeDesVilles) 
    # for i in range(1,len(listeDesVilles)):
    #     nombreDesPossibles *= (i)
    nombreDesPossibles = math.factorial(len(listeDesVilles)-1)
    copy.copy(listeDesVilles)
    # while ()

    print(nombreDesPossibles)

createAllPathForOneCity(getListDesVilles(listinstruction))

