points = {'A': 1, 'B': 2,'C': 3, 'X': 1,'Y': 2, 'Z': 3}
file1 = open('Day 2/input.txt', 'r')
lines = file1.readlines()
file1.close()
score = 0
for line in lines:
    game = line.split()
    score += points[game[1]]
    if points[game[0]] == points[game[1]]:
        score += 3 #draw
    elif game[0] == 'A' and game[1] == 'Y' or game[0] == 'B' and game[1] == 'Z' or game[0] == 'C' and game[1] == 'X':
        score += 6 #win
print(score)