from import2 import chaine
import copy
import re
chaine2 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
listinstruction = chaine.splitlines()
#listinstruction = chaine2.splitlines()

numbersOfCubes = {}
numbersOfCubes['red'] =12
numbersOfCubes['green'] = 13
numbersOfCubes['blue'] = 14

def isItPossible(numbersOfCubes):
    for color in numbersOfCubes:
        if numbersOfCubes[color] < 0:
            return False
    return True

compteur = 0 

for instruction in listinstruction:
    
    game = instruction.split(":")
    listNumberGame = game[0].split()
    GameNumber = int(listNumberGame[1])
    gameinstruction = game[1].split(";")
    gameIsPossible = True
    for gameset in gameinstruction:
        numbersOfCubesGame = copy.copy(numbersOfCubes)
        gameset = gameset.split()

        for i in range(len(gameset)):
            if gameset[i].isdigit():
                color = gameset[i+1].replace(",", "")
                #color = re.sub(pattern, "", gameset[i+1])
                #print(gameset[i+1].replace(",", ""))
                numbersOfCubesGame[color] -= int(gameset[i])
            #print("ici")

        if not isItPossible(numbersOfCubesGame):
            # print(numbersOfCubesGame)
            # print(GameNumber)
            gameIsPossible = False


    if gameIsPossible:
        # print(numbersOfCubesGame)
        #print("possible " , GameNumber)
        compteur += GameNumber

print(compteur)

# part 2 

numbersOfCubes = {}
numbersOfCubes['red'] = 0
numbersOfCubes['green'] = 0
numbersOfCubes['blue'] = 0
compteur = 0 

for instruction in listinstruction:
    game = instruction.split(":")
    gameinstruction = game[1].split(";")
    numbersOfCubesGame = copy.copy(numbersOfCubes)
    for gameset in gameinstruction:
        gameset = gameset.split()
        for i in range(len(gameset)):
            if gameset[i].isdigit():
                color = gameset[i+1].replace(",", "")
                if numbersOfCubesGame[color] < int(gameset[i]):
                    numbersOfCubesGame[color] = int(gameset[i])
    
    compteur += numbersOfCubesGame['green'] * numbersOfCubesGame['blue'] * numbersOfCubesGame['red']


print(compteur)
