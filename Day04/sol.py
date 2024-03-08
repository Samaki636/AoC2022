import re
count = 0
countPart2 = 0
with open("AoC2022/Day04/input02.txt") as infile:
    for line in infile:
        n1, n2, n3, n4 = (int(s) for s in re.split('-|,', line))
        if (n3 >= n1 and n4 <= n2) or (n3 <= n1 and n4 >= n2):
            count += 1
        if (n1 <= n3 <= n2) or (n1 <= n4 <= n2) or (n3 >= n1 and n4 <= n2) or (n3 <= n1 and n4 >= n2):
            countPart2 += 1
print(count)
print(countPart2)