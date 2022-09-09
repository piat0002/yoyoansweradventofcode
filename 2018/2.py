from import2 import chaine

# dictionnaire = {}

# dictionnaire['lol'] = 1

# print(dictionnaire)

# if 'pol' not in dictionnaire:
#     print('test')

listinstruction = chaine.splitlines()

deuxC = 0
troisC = 0
for i in listinstruction:
    dictionnaire = {}
    for j in i:
        if j not in dictionnaire:
            dictionnaire[j] = 1
        else:
            dictionnaire[j] += 1
    
   # print(dictionnaire)
    deuxplus = True
    troisplus = True
    for x, y in dictionnaire.items():
        #print(x, y )
        if y == 2 and deuxplus:
            deuxC += 1
            deuxplus = False
        elif y == 3 and troisplus:
            troisC += 1
            troisplus = False

#print(deuxC,troisC)
print(deuxC * troisC)