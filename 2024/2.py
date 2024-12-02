from import2 import chaine
import math
import copy
chaine2 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
listinstruction = chaine.splitlines()
#listinstruction = chaine2.splitlines()


compteur = 0
for instruction in listinstruction:
    instrusplit = instruction.split()
    IsSafe = True
    if int(instrusplit[0]) < int(instrusplit[1]):
        for i in range(1,len(instrusplit)):
            # print(instrusplit[i-1]+" "+instrusplit[i])
            # print(int(instrusplit[i-1]) < int(instrusplit[i]))
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                IsSafe = False
            if not(int(instrusplit[i-1]) < int(instrusplit[i])):
                IsSafe = False

    elif not int(instrusplit[0]) == int(instrusplit[1]):
        for i in range(1,len(instrusplit)):
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                IsSafe = False
            if not (int(instrusplit[i-1]) > int(instrusplit[i])):
                IsSafe = False
    else:
        IsSafe = False
    if IsSafe:
        #print(instruction)
        compteur += 1
print(compteur)

# part 2 

# cest pas opti mais je pense que un systeme de point peut marché dans ce probleme 
# ca permet de tolerer les erreurs
def isIncreasing(liste):
    increaseCount = 0
    decreaseCount = 0
    for i in range(1,len(liste)):
        if int(liste[i-1]) < int(liste[i]):
            increaseCount += 1
        elif int(liste[i-1]) > int(liste[i]):
            decreaseCount += 1

    if increaseCount > decreaseCount:
        return "i"
    elif decreaseCount > increaseCount:
        return "d"
    else:
        return "e"

def suprimeIEtVerif(isIncreasingVar,instrusliste,i):
    instrusplit = copy.copy(instrusliste)
    instrusplit.pop(i)
    #print(instrusplit)
    if isIncreasingVar == "i":
        for i in range(1,len(instrusplit)):
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                return False
            if not(int(instrusplit[i-1]) < int(instrusplit[i])):
                return False

    elif isIncreasingVar == "d":
        for i in range(1,len(instrusplit)):
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                return False
            if not (int(instrusplit[i-1]) > int(instrusplit[i])):
                return False
    else:
        return False
    return True



#listinstruction = chaine2.splitlines()
compteur = 0
for instruction in listinstruction:
    instrusplit = instruction.split()
    #print(isIncreasing(instrusplit))
    IsSafe = 0
    isIncreasingVar = isIncreasing(instrusplit)
    if isIncreasingVar == "i":
        for i in range(1,len(instrusplit)):
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                IsSafe += 1
                lindexasup = i
                break
            if not(int(instrusplit[i-1]) < int(instrusplit[i])):
                IsSafe += 1
                lindexasup = i
                break

    elif isIncreasingVar == "d":
        for i in range(1,len(instrusplit)):
            if math.fabs(int(instrusplit[i-1]) - int(instrusplit[i])) > 3:
                IsSafe += 1
                lindexasup = i
                break
            if not (int(instrusplit[i-1]) > int(instrusplit[i])):
                IsSafe += 1
                lindexasup = i
                break
    else:
        IsSafe += len(instrusplit)
    
    if IsSafe == 0:
        #print(instruction)
        compteur += 1
    elif IsSafe == 1:
        #print(instruction)
        #print(lindexasup)
        if suprimeIEtVerif(isIncreasingVar,instrusplit,lindexasup-1) or suprimeIEtVerif(isIncreasingVar,instrusplit,lindexasup):
            #print(instruction)
            compteur += 1
            
        
print(compteur)

    
