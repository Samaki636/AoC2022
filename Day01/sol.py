calPerElf = []
with open("AoC2022/Day01/input02.txt") as inputFile:
    totCal = 0
    for line in inputFile:
        if line.strip():
            totCal += int(line)
        else:
            calPerElf.append(totCal)
            totCal = 0    
calPerElf.append(totCal)
print(max(calPerElf))
calPerElf.sort()
sum = calPerElf[-1]+calPerElf[-2]+calPerElf[-3]
print(sum)