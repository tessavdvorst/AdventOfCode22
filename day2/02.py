# opponent rock = A
# opponent paper = B
# opponent scissor = C

# my rock = 1
# my paper = 2
# my scissor = 3

# lost = X = 0
# draw = Y = 3
# win = Z = 6

choices = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}
score = 0
with open("input.txt", 'r') as input:
    guide = [x.strip('\n') for x in input]
for line in guide:
    score += choices.get(line)
print(score)