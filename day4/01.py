with open("test.txt", 'r') as input:
    list_of_pairs = [x.strip('\n').split(',') for x in input]
print(list_of_pairs)

for pair in list_of_pairs:
    