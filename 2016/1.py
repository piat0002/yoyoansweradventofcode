from import1 import chaine

listinstruction = chaine.split(', ')

# print(listinstruction)


degree = 90

x,y= 0,0
for i in listinstruction:
    instruction = list(i)
    
    if instruction[0] == 'R':
        degree = (degree - 90) % 360
        # print('lol')

    else : 
        degree = (degree + 90) % 360

    print(instruction)

    # print(''.join(instruction[1:]))
    if degree == 0:
        x = x + (1 * int(''.join(instruction[1:])))
    elif degree == 90:
        y = y + (1 * int(''.join(instruction[1:])))
    elif degree == 180:
        x = x - (1 * int(''.join(instruction[1:])))
    else :
        y = y - (1 * int(''.join(instruction[1:])))
    print(x,y)
distance = abs(x) + abs(y)

print("la distance", distance)


w, h = 500, 500
MyMatrix = [ [0 for x in range( w )] for y in range( h ) ]  


degree = 90

x,y= 250,250
for i in listinstruction:
    instruction = list(i)
    
    if instruction[0] == 'R':
        degree = (degree - 90) % 360
        # print('lol')

    else : 
        degree = (degree + 90) % 360

    # print(''.join(instruction[1:]))
    print(instruction)

    if degree == 0:
        # x = x + (1 * int(''.join(instruction[1:])))

        for i in range(x, x +  int(''.join(instruction[1:]))):
            x += 1
            if MyMatrix[x][y] == 1:
                print('ok')
                break
            MyMatrix[x][y] += 1
        else:
            continue
        break
        
    elif degree == 90:
        # y = y + (1 * int(''.join(instruction[1:])))

        for i in range(y, y +  int(''.join(instruction[1:]))):
            y += 1
            if MyMatrix[x][y] == 1:
                print('ok')
                break

            MyMatrix[x][y] += 1
        else:
            continue
        break

    elif degree == 180:
        # x = x - (1 * int(''.join(instruction[1:])))

        for i in range(x, x -  int(''.join(instruction[1:])) , -1):
            x -= 1
            if MyMatrix[x][y] == 1:
                print('mol')
                # print(x,y)
                break
            MyMatrix[x][y] += 1
        else:
            continue
        break

    else :
        # y = y - (1 * int(''.join(instruction[1:])))

        for i in range(y, y -  int(''.join(instruction[1:])) , -1):
            y -= 1
            if MyMatrix[x][y] == 1:
                print('lol')
                break

            MyMatrix[x][y] += 1
        else:
            continue
        break

print(x,y)

distance = abs(x -250) + abs(y -250)
print("la nouvelle distance", distance)
