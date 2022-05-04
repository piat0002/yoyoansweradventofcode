from import1 import chaine
number = 0
number2 = 0
for i in range(len(chaine.splitlines())):
    for j in range(len(chaine.splitlines())):
        if ( int(chaine.splitlines()[i])+int(chaine.splitlines()[j]) )  == 2020:
            number =int(chaine.splitlines()[i])
            number2 = int(chaine.splitlines()[j])

print(number)
print(number2)


print(number * number2)
number = 0
number2 = 0
for i in range(len(chaine.splitlines())):
    for j in range(len(chaine.splitlines())):
        for k in range(len(chaine.splitlines())):
            if ( int(chaine.splitlines()[i])+int(chaine.splitlines()[j])+int(chaine.splitlines()[k]))  == 2020:
                number =int(chaine.splitlines()[i])
                number2 = int(chaine.splitlines()[j])
                number3 = int(chaine.splitlines()[k])
                print("lol")
                break
        else:
            continue
        break
    else:
        continue
    break
print(number)
print(number2)
print(number3)

print(number * number2 * number3)