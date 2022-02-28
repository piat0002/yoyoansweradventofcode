# c'est pas ma solution

instruction = open('inputs/pmroble8-input')

print(instruction)

# for s in instruction:
#     print(s[:-1])

print(instruction.read())

print(sum(len(s[:-1]) - len(eval(s)) for s in open('inputs/pmroble8-input')))
print(sum(2+s.count('\\')+s.count('"') for s in open('inputs/pmroble8-input')))