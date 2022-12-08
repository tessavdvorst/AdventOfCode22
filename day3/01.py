# store the input in a list without new line char
# for every line, split in half and store in list
#   check which char appears in both lists.
#   convert the char to the priority score and add to sum
# print (sum)

import math

with open("test.txt", 'r') as input:
    list_of_rucksacks = [x.strip('\n') for x in input]
for rucksack in list_of_rucksacks:
    middle_index = math.floor(len(rucksack) / 2)
    rucksack.slice(:middle_index)
print(list_of_rucksacks)