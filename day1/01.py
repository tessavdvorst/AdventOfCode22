f = open("input.txt", 'r')
arr_calories = f.readlines()

elf = []
arr_total_cal = []
for line in arr_calories:
    if line == "\n":
        arr_total_cal.append(sum(elf))
        elf.clear()
        continue
    elf.append(int(line[:-1]))
arr_total_cal.sort(reverse=True)
print(arr_total_cal[0])

