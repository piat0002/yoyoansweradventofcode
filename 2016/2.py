from import2 import chaine

# chaine = """ULL
# RRDDD
# LURDL
# UUUUD"""

instructionsPourUnNumero = chaine.splitlines()

tableau =  [[1,2,3],
            [4,5,6],
            [7,8,9]]

chiffreIndex = [1,1] 

def up():
    chiffreIndex[0] -= 0 if chiffreIndex[0] == 0 else 1
def down():
    chiffreIndex[0] += 0 if chiffreIndex[0] == len(tableau) - 1 else 1
def left():
    chiffreIndex[1] -= 0 if chiffreIndex[1] == 0 else 1
def righ():
    chiffreIndex[1] += 0 if chiffreIndex[1] == len(tableau[0]) - 1 else 1


code = ''
for instruction in instructionsPourUnNumero:
    for lettre in instruction:
        if lettre == 'U':
            up()
        elif lettre == 'R':
            righ()       
        elif lettre == 'D':
            down()
        else:
            left()

    #print(chiffreIndex)
    #print(tableau[chiffreIndex[0]][chiffreIndex[1]])

    code += str(tableau[chiffreIndex[0]][chiffreIndex[1]])
    
print(code)


tableau2 =  [['N','N','1','N','N'],
             ['N','2','3','4','N'],
             ['5','6','7','8','9'],
             ['N','A','B','C','N'],
             ['N','N','D','N','N'],
    ]

chiffreIndex2 = [2,0] 

def up2():
    chiffreIndex2[0] -= 0 if chiffreIndex2[0] == 0 else 1
    #print(chiffreIndex2)
    chiffreIndex2[0] += 1 if tableau2[chiffreIndex2[0]][chiffreIndex2[1]] == 'N' else 0
def down2():
    chiffreIndex2[0] += 0 if chiffreIndex2[0] == len(tableau2) - 1 else 1
    chiffreIndex2[0] -= 1 if tableau2[chiffreIndex2[0]][chiffreIndex2[1]] == 'N' else 0
def left2():
    chiffreIndex2[1] -= 0 if chiffreIndex2[1] == 0 else 1
    chiffreIndex2[1] += 1 if tableau2[chiffreIndex2[0]][chiffreIndex2[1]] == 'N' else 0
def righ2():
    chiffreIndex2[1] += 0 if chiffreIndex2[1] == len(tableau2[0]) - 1 else 1
    chiffreIndex2[1] -= 1 if tableau2[chiffreIndex2[0]][chiffreIndex2[1]] == 'N' else 0


code2 = ''

for instruction in instructionsPourUnNumero:
    for lettre in instruction:
        if lettre == 'U':
            up2()
        elif lettre == 'R':
            righ2()       
        elif lettre == 'D':
            down2()
        else:
            left2()

    #print(chiffreIndex2)
    #print(tableau2[chiffreIndex2[0]][chiffreIndex2[1]])
    code2 += tableau2[chiffreIndex2[0]][chiffreIndex2[1]]

print(code2)