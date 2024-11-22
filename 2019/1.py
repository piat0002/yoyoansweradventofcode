import math
from import1 import chaine

listinstruction = chaine.splitlines()

def calculFuel(instruction):
    division =  math.floor(int(instruction) / 3)
    return division - 2

# print(calculFuel(1969))
# print(calculFuel(100756))
compteur = 0
for instruction in listinstruction:
    compteur += calculFuel(instruction)
    
print(compteur)

# part 2

compteur = 0
# listinstruction = [1969]
for instruction in listinstruction:
    moduleOfMass = 0
    requires = int(instruction)
    while requires >= 0: 
        # print(requires)
        requires = math.floor(int(requires) / 3)
        requires -= 2
        if requires >= 0:
            moduleOfMass += math.fabs(requires) 
    compteur += moduleOfMass

print(compteur)