file1 = open('Day 6/input.txt', 'r')
lines = file1.readlines()
file1.close()
temp = []
for i in range(14):
    temp.append(lines[0][i])

for i in range(14, len(lines[0])):
    if len(set(temp)) == 14:
        print(i)
        break
    del temp[0]
    temp.append(lines[0][i])