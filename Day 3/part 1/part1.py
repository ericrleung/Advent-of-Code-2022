points = {'a': 1, 'b': 2,'c': 3, 'd': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8,'i': 9, 'j': 10,'k': 11, 'l': 12, 'm': 13,
'n': 14, 'o': 15,'p': 16, 'q': 17,'r': 18, 's': 19, 't': 20, 'u': 21,'v': 22, 'w': 23,'x': 24, 'y': 25, 'z': 26}
file1 = open('Day 3/part 1/input.txt', 'r')
lines = file1.readlines()
file1.close()
priorities = 0
for line in lines:
    line1 = line[:len(line) // 2]
    line2 = line[len(line) // 2:]
    for char in line1:
        if char in line2:
            print(char)
            if char.lower() != char:
                priorities += 26
            priorities += points[char.lower()]
            break
print(priorities)