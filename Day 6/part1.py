file1 = open('Day 6/input.txt', 'r')
lines = file1.readlines()
file1.close()
first = lines[0][0]
second = lines[0][1]
third = lines[0][2]
fourth = lines[0][3]

for i in range(4, len(lines[0])):
    if len(set([first, second, third, fourth])) == 4:
        print(i)
        break
    fourth, third, second, first = lines[0][i], fourth, third, second
