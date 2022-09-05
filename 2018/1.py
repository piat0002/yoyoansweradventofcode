from import1 import chaine


# chaine = """"+7
# +7
# -2
# -7
# -4"""

# chaine = """+1
# -2
# +3
# +1"""


listinstruction = chaine.splitlines()

frequence = 0
for i in listinstruction:
    if i[0] == '+':
        #print(i[1:])
        frequence += int(i[1:]) 
    else:
        frequence -= int(i[1:])
print(frequence)

## part 2

frequence = 0
alreadySeen = [0]
compteur = 0
while True:
    #print(frequence)
    if listinstruction[compteur][0] == '+':
        #print(i[1:])
        frequence += int(listinstruction[compteur][1:]) 
    else:
        frequence -= int(listinstruction[compteur][1:])
    if frequence in alreadySeen:
        print(frequence)
        break
    alreadySeen.append(frequence)
    compteur += 1
    if compteur == len(listinstruction):
        compteur = 0

print(frequence)

## the time to resolve is big but its work in my case its 464