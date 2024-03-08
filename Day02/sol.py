with open("AoC2022/Day02/input02.txt") as inputFile:
    totScoreP2 = 0
    totScoreP2Part2 = 0
    for line in inputFile:
        scoreP1 = ord(line[0])-ord('@')
        scoreP2 = ord(line[2])-ord('W')
        totScoreP2 += scoreP2
        if scoreP1 == scoreP2:
            totScoreP2 += 3
        if scoreP1 - scoreP2 in (-1, 2):
            totScoreP2 += 6
        match line[2]:
            case 'X':
                match line[0]:
                    case 'A':
                        totScoreP2Part2+=3
                    case 'B':
                        totScoreP2Part2+=1
                    case 'C':
                        totScoreP2Part2+=2
            case 'Y':
                match line[0]:
                    case 'A':
                        totScoreP2Part2+=4
                    case 'B':
                        totScoreP2Part2+=5
                    case 'C':
                        totScoreP2Part2+=6
            case 'Z':
                match line[0]:
                    case 'A':
                        totScoreP2Part2+=8
                    case 'B':
                        totScoreP2Part2+=9
                    case 'C':
                        totScoreP2Part2+=7
print(totScoreP2)
print(totScoreP2Part2)