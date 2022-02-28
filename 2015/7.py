from import7 import chaine

# chaine = """x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# 123 -> x
# 456 -> y
# """

listinstruction = chaine.splitlines()

dico = {}

def converstion16bit(inte):
    return format(inte, '016b')

def ifnot(array):
    return array[0] == "NOT"

def isSimpleAffectation(array):
    return array[1] == "->"

def isAnd(array):
    return array[1] == 'AND'

def isOr(array):
    return array[1] == 'OR'

def isLSHIFT(array):
    return array[1] == "LSHIFT"

def isRSHIFT(array):
    return array[1] == "RSHIFT"

def isExistInDico(key):
    return key in dico

def analyse(array):
    if ifnot(array):
        return 'ok'
    elif isSimpleAffectation(array):
        return 'ok'

def bin16Not(string):
    retour = ''
    for chiffre in string:
        if chiffre == '1':
            retour += '0'  
        elif chiffre == '0': 
            retour += '1'  
    return retour

def bin16LS(string, number):
    return  string[number : len(string)] +( number * '0' )

def bin16RS(string, number):
    #print('0123456789abcdef'[0 : 15])
    #[a,b] ok c'est b est exclus
    return "0" * number + string[0 : len(string) - number]

def bin16OR(string1,string2):
    retour = ''
    for i in range(16):
        if string1[i] == '1' or string2[i] == '1':
            retour += '1'
        else :
            retour += '0'
    return retour
    
def bin16AND(string1,string2):
    retour = ''
    for i in range(16):
        if string1[i] == '1' and string2[i] == '1':
            retour += '1'
        else :
            retour += '0'
    return retour
# x,y = '0000000001111011' ,'0000000111001000'
# print(int(bin16OR(x,y), 2))
# listinstruction.pop(1)
# print(len(listinstruction))
while len(listinstruction) != 0:
    i = 0
    #print(len(listinstruction))
    while i < len(listinstruction):
        if ifnot(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[1]
            #print(key)
            if not key.isdigit():              
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16Not(dico[key])
                    
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16Not(converstion16bit(int(key)))
                listinstruction.pop(i)
                i -= 1
        
        elif isSimpleAffectation(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            #print(key)
            if key.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = converstion16bit(int(key))
                listinstruction.pop(i)
                i -= 1
            elif isExistInDico(key):
                dico[listinstruction[i].split(" ")[-1]] = dico[key]
                listinstruction.pop(i)
                i -= 1

        elif isLSHIFT(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            chiffre = int(listinstruction[i].split(" ")[2])
            if not key.isdigit():
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16LS(dico[key],chiffre)
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16LS(converstion16bit(int(key)),chiffre)
                listinstruction.pop(i)
                i -= 1

        elif isRSHIFT(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            chiffre = int(listinstruction[i].split(" ")[2])
            if not key.isdigit():
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16RS(dico[key],chiffre)
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16RS(converstion16bit(int(key)),chiffre)
                listinstruction.pop(i)
                i -= 1

        elif isOr(listinstruction[i].split(" ")):
            key1 = listinstruction[i].split(" ")[0]
            key2 = listinstruction[i].split(" ")[2]
            #print(listinstruction[i].split(" ")[-1])
            if key1.isdigit() and key2.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = bin16OR(converstion16bit(int(key1)),converstion16bit(int(key2)))

                listinstruction.pop(i)
                i -= 1

            elif key1.isdigit():
                if isExistInDico(key2):
                    dico[listinstruction[i].split(" ")[-1]] = bin16OR(converstion16bit(int(key1)),dico[key2])
            
                    listinstruction.pop(i)
                    i -= 1

            elif key2.isdigit():
                if isExistInDico(key1):
                    dico[listinstruction[i].split(" ")[-1]] = bin16OR(dico[key1],converstion16bit(int(key2)))

                    listinstruction.pop(i)
                    i -= 1
            else :
                if isExistInDico(key1):
                    if isExistInDico(key2):
                        dico[listinstruction[i].split(" ")[-1]] = bin16OR(dico[key1],dico[key2])
                        
                        listinstruction.pop(i)
                        i -= 1
    

        elif isAnd(listinstruction[i].split(" ")):
            key1 = listinstruction[i].split(" ")[0]
            key2 = listinstruction[i].split(" ")[2]
            #print(listinstruction[i].split(" ")[-1])
            if key1.isdigit() and key2.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = bin16AND(converstion16bit(int(key1)),converstion16bit(int(key2)))

                listinstruction.pop(i)
                i -= 1

            elif key1.isdigit():
                if isExistInDico(key2):
                    dico[listinstruction[i].split(" ")[-1]] = bin16AND(converstion16bit(int(key1)),dico[key2])
            
                    listinstruction.pop(i)
                    i -= 1

            elif key2.isdigit():
                if isExistInDico(key1):
                    dico[listinstruction[i].split(" ")[-1]] = bin16AND(dico[key1],converstion16bit(int(key2)))

                    listinstruction.pop(i)
                    i -= 1
            else :
                if isExistInDico(key1):
                    if isExistInDico(key2):
                        dico[listinstruction[i].split(" ")[-1]] = bin16AND(dico[key1],dico[key2])
                        
                        listinstruction.pop(i)
                        i -= 1

        else:
            print('error stop script')
        # print(len(listinstruction))
        # print(listinstruction  )
        i += 1
        #print(dico)

print(dico)
#print(len(dico['g']))
print(int(dico['a'], 2))

#print(isExistInDico("fz"))
#temp = converstion16bit(10)
#print(temp)

from import7b import chaine
listinstruction = chaine.splitlines()
dico = {}


while len(listinstruction) != 0:
    i = 0
    #print(len(listinstruction))
    while i < len(listinstruction):
        if ifnot(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[1]
            #print(key)
            if not key.isdigit():              
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16Not(dico[key])
                    
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16Not(converstion16bit(int(key)))
                listinstruction.pop(i)
                i -= 1
        
        elif isSimpleAffectation(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            #print(key)
            if key.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = converstion16bit(int(key))
                listinstruction.pop(i)
                i -= 1
            elif isExistInDico(key):
                dico[listinstruction[i].split(" ")[-1]] = dico[key]
                listinstruction.pop(i)
                i -= 1

        elif isLSHIFT(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            chiffre = int(listinstruction[i].split(" ")[2])
            if not key.isdigit():
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16LS(dico[key],chiffre)
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16LS(converstion16bit(int(key)),chiffre)
                listinstruction.pop(i)
                i -= 1

        elif isRSHIFT(listinstruction[i].split(" ")):
            key = listinstruction[i].split(" ")[0]
            chiffre = int(listinstruction[i].split(" ")[2])
            if not key.isdigit():
                if isExistInDico(key):
                    dico[listinstruction[i].split(" ")[-1]] = bin16RS(dico[key],chiffre)
                    listinstruction.pop(i)
                    i -= 1
            else:
                dico[listinstruction[i].split(" ")[-1]] = bin16RS(converstion16bit(int(key)),chiffre)
                listinstruction.pop(i)
                i -= 1

        elif isOr(listinstruction[i].split(" ")):
            key1 = listinstruction[i].split(" ")[0]
            key2 = listinstruction[i].split(" ")[2]
            #print(listinstruction[i].split(" ")[-1])
            if key1.isdigit() and key2.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = bin16OR(converstion16bit(int(key1)),converstion16bit(int(key2)))

                listinstruction.pop(i)
                i -= 1

            elif key1.isdigit():
                if isExistInDico(key2):
                    dico[listinstruction[i].split(" ")[-1]] = bin16OR(converstion16bit(int(key1)),dico[key2])
            
                    listinstruction.pop(i)
                    i -= 1

            elif key2.isdigit():
                if isExistInDico(key1):
                    dico[listinstruction[i].split(" ")[-1]] = bin16OR(dico[key1],converstion16bit(int(key2)))

                    listinstruction.pop(i)
                    i -= 1
            else :
                if isExistInDico(key1):
                    if isExistInDico(key2):
                        dico[listinstruction[i].split(" ")[-1]] = bin16OR(dico[key1],dico[key2])
                        
                        listinstruction.pop(i)
                        i -= 1
    

        elif isAnd(listinstruction[i].split(" ")):
            key1 = listinstruction[i].split(" ")[0]
            key2 = listinstruction[i].split(" ")[2]
            #print(listinstruction[i].split(" ")[-1])
            if key1.isdigit() and key2.isdigit():
                dico[listinstruction[i].split(" ")[-1]] = bin16AND(converstion16bit(int(key1)),converstion16bit(int(key2)))

                listinstruction.pop(i)
                i -= 1

            elif key1.isdigit():
                if isExistInDico(key2):
                    dico[listinstruction[i].split(" ")[-1]] = bin16AND(converstion16bit(int(key1)),dico[key2])
            
                    listinstruction.pop(i)
                    i -= 1

            elif key2.isdigit():
                if isExistInDico(key1):
                    dico[listinstruction[i].split(" ")[-1]] = bin16AND(dico[key1],converstion16bit(int(key2)))

                    listinstruction.pop(i)
                    i -= 1
            else :
                if isExistInDico(key1):
                    if isExistInDico(key2):
                        dico[listinstruction[i].split(" ")[-1]] = bin16AND(dico[key1],dico[key2])
                        
                        listinstruction.pop(i)
                        i -= 1

        else:
            print('error stop script')
        # print(len(listinstruction))
        # print(listinstruction  )
        i += 1
        #print(dico)

print(dico)
#print(len(dico['g']))
print(int(dico['a'], 2))

#print(isExistInDico("fz"))
#temp = converstion16bit(10)
#print(temp)