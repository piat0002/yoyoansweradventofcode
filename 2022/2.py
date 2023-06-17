from import2 import chaine

# chaine = """A Y
# B X
# C Z"""

listinstruction = chaine.splitlines()

def ajoutpoint(jeu):
    point = 0
    #A rock B paper  C scissor
    opponent = jeu[0]
    #Y paper   X ROCK Z scissor 
    me = jeu[2]
    #win
    if (me == "Y" and opponent == "A") or (me == "X" and opponent == "C") or (me == "Z" and opponent == "B"):
        point = 6
    elif (me == "Y" and opponent == "B")  or (me == "X" and opponent == "A") or (me == "Z" and opponent == "C"):
        point = 3 

    #les point ajouté du au choi
    if me == "X":
        point += 1
    elif me == "Y":
        point += 2
    else :
        point += 3
    return point

amount = 0
for i in listinstruction:
    amount += ajoutpoint(i)

print(amount)

#part2

def ajoutpoint2(jeu):
    point = 0
    #A rock B paper  C scissor
    opponent = jeu[0]
    #Y  draw  X  loose Z  win
    me = jeu[2]
    if me == "Z" :
        point = 6
    elif me == "Y":
        point = 3



    #les point ajouté du au choi
    if (point == 6 and opponent == "C" ) or (point == 3 and opponent == "A") or (point == 0 and opponent == "B"):
        point += 1
    elif (point == 6 and opponent == "A" ) or (point == 3 and opponent == "B") or (point == 0 and opponent == "C"):     
        point += 2
    else :
        point += 3
    return point

amount = 0
for i in listinstruction:
    amount += ajoutpoint2(i)

print(amount)