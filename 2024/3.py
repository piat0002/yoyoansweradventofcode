from import2 import chaine
import re
with open('2024/import3', 'r') as file:
    chaine = file.read()

chaine2 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
#chaine = chaine2

pattern = r"mul\(\d{1,6},\d{1,6}\)"
matches = re.findall(pattern,chaine, re.MULTILINE)

#print(matches)

compteur = 0
for matche in matches:
    patternNumber = r"\d{1,6}"
    numbers = re.findall(patternNumber,matche, re.MULTILINE)
    compteur += int(numbers[0]) * int(numbers[1])

print(compteur)

#part2

chaine3 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
#chaine = chaine3
pattern3 = r"mul\(\d{1,6},\d{1,6}\)|do\(\)|don't\(\)"

matches = re.findall(pattern3,chaine, re.MULTILINE)

#print(matches)

do = True
patternNumber = r"\d{1,6}"
compteur = 0
for matche in matches:
    # print(matche)
    if matche == "don't()":
        do = False
    elif matche == 'do()':
        do = True
    elif do:
        # print("cal")
        # print(compteur)
        numbers = re.findall(patternNumber,matche, re.MULTILINE)
        compteur += int(numbers[0]) * int(numbers[1])


print(compteur)