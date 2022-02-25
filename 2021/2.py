from import2 import chaine



listinstruction = chaine.splitlines()

#print(listinstruction)
forward = 0
depth = 0


for instruction in listinstruction:
    arrayinstru = instruction.split(' ')
    #print(arrayinstru)
    if arrayinstru[0] == "down":
        depth -= int(arrayinstru[1])
    elif arrayinstru[0] == 'up':
        depth += int(arrayinstru[1])
    else:
        forward += int(arrayinstru[1])

print(depth )
print( forward) 
print(depth * forward)

listinstruction = chaine.splitlines()

#print(listinstruction)
forward = 0
depth = 0
aim = 0


for instruction in listinstruction:
    arrayinstru = instruction.split(' ')
    #print(arrayinstru)
    if arrayinstru[0] == "down":
        aim += int(arrayinstru[1])
    elif arrayinstru[0] == 'up':
        aim -= int(arrayinstru[1])
    else:
        forward += int(arrayinstru[1])
        depth += int(arrayinstru[1]) * aim



print(depth )
print( forward) 
print(depth * forward)