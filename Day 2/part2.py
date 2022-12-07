points = {'X': 0,'Y': 3, 'Z': 6}
#1 rock, 2paper, 3 scissors
file1 = open('Day 2/input.txt', 'r')
lines = file1.readlines()
file1.close()
score = 0
for line in lines:
    game = line.split()
    score += points[game[1]]
    if game[0] == 'A' and game[1] == 'X':
        score += 3
    elif game[0] == 'A' and game[1] == 'Y':
        score += 1
    elif game[0] == 'A' and game[1] == 'Z':
        score += 2
    elif game[0] == 'B' and game[1] == 'X':
        score += 1
    elif game[0] == 'B' and game[1] == 'Y':
        score += 2
    elif game[0] == 'B' and game[1] == 'Z':
        score += 3
    elif game[0] == 'C' and game[1] == 'X':
        score += 2
    elif game[0] == 'C' and game[1] == 'Y':
        score += 3
    elif game[0] == 'C' and game[1] == 'Z':
        score += 1
print(score)