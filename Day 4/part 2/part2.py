file1 = open('Day 4/part 1/input.txt', 'r')
lines = file1.readlines()
file1.close()
pairs = 0
for line in lines:
    ranges = line.split(",")
    first = ranges[0].split("-")
    second = ranges[1].split("-")
    # First in second
    if (int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]) or int(first[1]) <= int(second[0]) and int(first[1]) >= int(second[1]) or 
    int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0]) or int(first[0]) <= int(second[1]) and int(first[1]) >= int(second[1])):
        pairs += 1
print(pairs)