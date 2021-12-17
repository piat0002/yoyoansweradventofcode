from import1 import chaine


listinstruction = chaine.splitlines()
compteur = 0
for i in range(len(listinstruction)-1):
    present = int(listinstruction[i]) 
    apres = int(listinstruction[i + 1])
    if(present < apres):
        compteur += 1
print(compteur)
    
     
#part 2 
compteur = 0

for i in range(len(listinstruction)-3):
    present = int(listinstruction[i]) + int(listinstruction[i + 1]) + int(listinstruction[i + 2])
    apres =  int(listinstruction[i + 1]) + int(listinstruction[i + 2]) + int(listinstruction[i + 3]) 
    
    if(present < apres):
        compteur += 1

print(compteur)

lol = """607
618
618
617
647
716
769
792
"""
compteur = 0
listinstruction = lol.splitlines()
for i in range(len(listinstruction)-3):
    present = int(listinstruction[i]) + int(listinstruction[i + 1]) + int(listinstruction[i + 2]) 
    apres =  int(listinstruction[i + 1]) + int(listinstruction[i + 2]) + int(listinstruction[i + 3])
    
    if(present < apres):
        compteur += 1

print(compteur)