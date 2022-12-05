file1 = open('Day 5/part 1/input.txt', 'r')
lines = file1.readlines()
file1.close()
stacks = [[], [], [], [], [], [], [], [], []]
stacks[0].append('B')
stacks[0].append('L')
stacks[0].append('D')
stacks[0].append('T')
stacks[0].append('W')
stacks[0].append('C')
stacks[0].append('F')
stacks[0].append('M')
stacks[1].append('N')
stacks[1].append('B')
stacks[1].append('L')
stacks[2].append('J')
stacks[2].append('C')
stacks[2].append('H')
stacks[2].append('T')
stacks[2].append('L')
stacks[2].append('V')
stacks[3].append('S')
stacks[3].append('P')
stacks[3].append('J')
stacks[3].append('W')
stacks[4].append('Z')
stacks[4].append('S')
stacks[4].append('C')
stacks[4].append('F')
stacks[4].append('T')
stacks[4].append('L')
stacks[4].append('R')
stacks[5].append('W')
stacks[5].append('D')
stacks[5].append('G')
stacks[5].append('B')
stacks[5].append('H')
stacks[5].append('N')
stacks[5].append('Z')
stacks[6].append('F')
stacks[6].append('M')
stacks[6].append('S')
stacks[6].append('P')
stacks[6].append('V')
stacks[6].append('G')
stacks[6].append('C')
stacks[6].append('N')
stacks[7].append('W')
stacks[7].append('Q')
stacks[7].append('R')
stacks[7].append('J')
stacks[7].append('F')
stacks[7].append('V')
stacks[7].append('C')
stacks[7].append('Z')
stacks[8].append('R')
stacks[8].append('P')
stacks[8].append('M')
stacks[8].append('L')
stacks[8].append('H')
for line in lines:
    lineSplit = line.split()
    amount = int(lineSplit[1])
    source = int(lineSplit[3]) - 1
    dest = int(lineSplit[5]) - 1
    temp = []
    for i in range(amount):
        temp.append(stacks[source].pop())
    for j in range(len(temp)):
        stacks[dest].append(temp.pop())
print(stacks)