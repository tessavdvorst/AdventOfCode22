# opponent rock = A
# opponent paper = B
# opponent scissor = C

# my rock = X = 1
# my paper = Y = 2
# my scissor = Z = 3

# lost = 0
# draw = 3
# win = 6

choices = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}
score = 0
with open("input.txt", 'r') as input:
    guide = [x.strip('\n') for x in input]
for line in guide:
    score += choices.get(line)
print(score)