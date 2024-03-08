result = 0
resultPart2 = 0
lines = []
i = 0
with open("AoC2022/Day03/input02.txt") as inputFile:
    for line in inputFile:
        firstPart, secondPart = line[:len(line)//2], line[len(line)//2:]
        for c in firstPart:
            if c in secondPart:
                if ord('a') <= ord(c) <= ord('z'):
                    result+=ord(c)-ord('a')+1
                else:
                    result+=ord(c)-ord('A')+27
                break

        lines.append(line)
        i+=1
        if i == 3:
            for c in lines[0]:
                if (c in lines[1]) and (c in lines[2]):
                    if ord('a') <= ord(c) <= ord('z'):
                        resultPart2+=ord(c)-ord('a')+1
                    else:
                        resultPart2+=ord(c)-ord('A')+27
                    break
            lines.clear()
            i = 0
print(result)
print(resultPart2)