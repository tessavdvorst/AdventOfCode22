import math

priority = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

with open("input.txt", 'r') as input:
    list_of_rucksacks = [x.strip('\n') for x in input]

i = 0
group = []
list_of_groups = []
for line in list_of_rucksacks:
    group.append(line)
    i += 1
    if i == 3:
        # print(group)
        list_of_groups.append(group)
        group = []
        i = 0

same_items = []
for group in list_of_groups:
    for i in range(0, len(group[0])):
        res = group[1].find(group[0][i])
        if res >= 0:
            res = group[2].find(group[1][res])
            if res >= 0:
                same_items.append(group[2][res])
                break   

sum_of_priorities = 0
for item in same_items:
    sum_of_priorities += priority.get(item)
print(sum_of_priorities)