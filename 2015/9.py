from import9 import chaine

from itertools import permutations


listinstruction = chaine.splitlines()
chaine2 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

chaine = chaine2
listinstruction = chaine2.splitlines()

def generateTableWithDistance(listinstruction):
    table = set()
    for instruction in listinstruction:
        tableinstruction = instruction.split()
        table.add(tableinstruction[0]) 
        table.add(tableinstruction[2])
    return table

print(generateTableWithDistance(listinstruction))

print(list(dict.fromkeys(generateTableWithDistance(listinstruction))))