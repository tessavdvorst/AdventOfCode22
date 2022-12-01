f = open("input.txt", 'r')
content = f.readlines()

total_elf = []
total_cal_all = []
for line in content:
    if line == "\n":
        total_cal_all.append(sum(total_elf))
        total_elf.clear()
        continue
    total_elf.append(int(line[:-1]))
total_cal_all.sort(reverse=True)
Sum = 0
for i in range(len(total_cal_all)):
    if i > 2:
        break
    Sum += int(total_cal_all[i])
print(Sum)