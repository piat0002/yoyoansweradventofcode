import hashlib
chaine = 'yzbqklnj'
print(hashlib.md5(b'abcdef609043').hexdigest())
print(hashlib.md5('pqrstuv1048970'.encode()).hexdigest())

compteur = 0
chainetohash = 'yzbqklnj' + str(compteur) 
#print(hashchaine)
hasttochaine = hashlib.md5(chainetohash.encode()).hexdigest()

#print(hasttochaine.hexdigest())
def condition(chaine):
    #print(chaine)
    retour = chaine[0] == '0' and chaine[1] == '0' and chaine[2] == '0' and chaine[3] == '0' and chaine[4] == '0'
    #print(retour)
    rlastcharactere = chaine[5] == '1' or chaine[5] == '2' or chaine[5] == '3' or chaine[5] == '4' or chaine[5] == '5' or chaine[5] == '6' or chaine[5] == '7' or chaine[5] == '8' or chaine[5] == '9'
    #print(rlastcharactere)
    retour = retour and rlastcharactere
    return retour

print(condition(hashlib.md5(b'abcdef609043').hexdigest()))
print(condition(hashlib.md5('pqrstuv1048970'.encode()).hexdigest()))


while not(condition(hashlib.md5(chainetohash.encode()).hexdigest())):
    compteur += 1
    chainetohash = 'yzbqklnj' + str(compteur) 

print(compteur)

def condition2(chaine):
    #print(chaine)
    retour = chaine[0] == '0' and chaine[1] == '0' and chaine[2] == '0' and chaine[3] == '0' and chaine[4] == '0'
    #print(retour)
    rlastcharactere = chaine [5]  == '0' 
    #print(rlastcharactere)
    retour = retour and rlastcharactere
    return retour

compteur = 0
while not(condition2(hashlib.md5(chainetohash.encode()).hexdigest())):
    compteur += 1
    chainetohash = 'yzbqklnj' + str(compteur) 

print(compteur)
