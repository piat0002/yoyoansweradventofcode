from import1 import chaine
import math
chaine2 = """3   4
4   3
2   5
1   3
3   9
3   3"""
listinstruction = chaine.splitlines()
#listinstruction = chaine2.splitlines()

liste1 = []
liste2 = []

#creation des liste
for instruction in listinstruction:
    listeInstru = instruction.split()
    liste1.append(int(listeInstru[0]))
    liste2.append(int(listeInstru[1]))


sliste1 = sorted(liste1)
sliste2 = sorted(liste2)

# print(liste1)
# print(liste2)
compteur = 0
for i in range(len(liste1)):
    compteur += math.fabs(sliste1[i] - sliste2[i])
print(compteur)


compteur = 0 
# part 2
for i in range(len(liste1)):
    x = liste2.count(liste1[i])
    compteur += liste1[i] * x
print(compteur)
