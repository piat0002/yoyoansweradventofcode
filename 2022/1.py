from import1 import chaine

listinstruction = chaine.splitlines()

mostgreatcalori = 0
amount = 0
for ligne in listinstruction:
    #print(ligne)
    if ligne == '':
        amount = 0
    else:
        amount += int(ligne)

    if mostgreatcalori < amount:
        mostgreatcalori = amount

print(mostgreatcalori)

## part 2

table = []
amount = 0
for ligne in listinstruction:
    if ligne == '':
        
        table.append(amount)
        amount = 0
    else:
        amount += int(ligne)

#[print(i) for i in sorted(table)]
table = sorted(table)
top3amount = table[len(table) - 1] + table[len(table) - 2] + table[len(table) - 3]
print(top3amount)