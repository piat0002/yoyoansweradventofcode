from import3 import chaine

listinstruction = chaine.splitlines()

def binNot(string):
    retour = ''
    for chiffre in string:
        if chiffre == '1':
            retour += '0'  
        elif chiffre == '0': 
            retour += '1'  
    return retour


# somme = 0
# gamma = 0
# epsilon = 0
# for l in listinstruction:
#     print(l)
#     if l[1] == '1':
#         gamma = int(l,2)
#         # epsilon = int(binNot(l),2)
       
#     else : 
#         epsilon += int(l,2)
# somme += gamma * epsilon 
#MyMatrix = [ [0 for x in range( w )] for y in range( h ) ] 


tableau = [[listinstruction[l][x] for l in range(len(listinstruction))] for x in range(len(listinstruction[0]))]

gamma = '' 
for liste in tableau :
    print(liste.count('1'))
    if liste.count('1') > len(liste)/2: 
        gamma += '1'
    else:
        gamma += '0'

epsilon = binNot(gamma)
somme = int(gamma,2) * int(epsilon,2) 


print(somme)