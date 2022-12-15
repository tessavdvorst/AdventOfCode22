from string import ascii_letters

with open("input.txt", 'r') as input:
    list_of_rucksacks = [x.strip('\n') for x in input]

i = 0
group = []
list_of_groups = []
for line in list_of_rucksacks:
    group.append(line)
    i += 1
    if i == 3:
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
for priority, char in enumerate(ascii_letters):
    for item in same_items:
        if item is char:
            sum_of_priorities += priority + 1

print("Answer for part 2: ", sum_of_priorities)