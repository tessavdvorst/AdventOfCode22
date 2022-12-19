# store data from file
with open("test.txt", 'r') as input:
    data = [line.strip('\n') for line in input.readlines()]

# get amount of stacks
columns = len(data[0])//4

# divide data
crate_data = data[:data.index('')-1]
instruction_data = data[data.index('')+1:]

for line in crate_data:
    line = list(line)[1:-1:4]
    print(line)



