file1 = open('Day 1/part 1/input.txt', 'r')
lines = file1.readlines()
file1.close()
current = 0
most = [0, 0, 0]
for line in lines:
    if line.strip() == "":
        if current > most[0]:
            most[1], most[2] = most[0], most[1]
            most[0] = current
        elif current > most[1]:
            most[2] = most[1]
            most[1] = current
        elif current > most[2]:
            most[2] = current
        current = 0
    else:
        current += int(line)
print(sum(most))