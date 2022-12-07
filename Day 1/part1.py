file1 = open('Day 1/input.txt', 'r')
lines = file1.readlines()
file1.close()
current = 0
most = 0
for line in lines:
    if line.strip() == "":
        if current > most:
            most = current
        current = 0
    else:
        current += int(line)
print(most)