f = open('test.txt', 'r')
calories = 0
largest = 0
num = 0
while(True):
    line = f.readline()
    if line == "":
        break
    if line == "\n":
        num += 1
        if num == 3:
            print ("calories = " + str(calories))
            if calories > largest:
                largest = calories
            calories = 0
            continue
    calories += int(line)
# print(largest)
f.close()