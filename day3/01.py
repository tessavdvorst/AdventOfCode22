from string import ascii_letters

with open("input.txt", 'r') as input:
    list_of_rucksacks = [x.strip('\n') for x in input]

all_split_rucksack = []
for line in list_of_rucksacks:
    rucksack = []
    middle_index = len(line)//2
    rucksack.append(line[:middle_index]) 
    rucksack.append(line[middle_index:])
    all_split_rucksack.append(rucksack) 

same_items = []
for rucksack in all_split_rucksack:
    for i in range(0, len(rucksack[0])):
        res = rucksack[1].find(rucksack[0][i])
        if res >= 0:
            same_items.append(rucksack[1][res])
            break

sum_of_priorities = 0
for priority, char in enumerate(ascii_letters):
    for item in same_items:
        if item is char:
            sum_of_priorities += priority + 1

print("Answer for part 1: ", sum_of_priorities)