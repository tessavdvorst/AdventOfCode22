with open("input.txt", 'r') as input:
    list_of_pairs = [x.strip('\n') for x in input]

count = 0
for pair in list_of_pairs:
    elf_one, elf_two = pair.split(',')
    elf_one = [int(i) for i in elf_one.split('-')]
    elf_two = [int(i) for i in elf_two.split('-')]
    if elf_one[0] >= elf_two[0] and \
    elf_one[0] <= elf_two[1]:
        count += 1
    elif elf_two[0] >= elf_one[0] and \
    elf_two[0] <= elf_one[1]:
        count += 1
print("Answer part 1: ", count)