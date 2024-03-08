import re
import copy

stacksN = 9
stacks = [[] for _ in range(stacksN)]
stacksPart2 = [[] for _ in range(stacksN)]
move = False
with open("AoC2022/Day05/input02.txt") as infile:
    for line in infile:
        if not line.strip():
            move = True
            for stack in stacks:
                stack.reverse()
            stacksPart2 = copy.deepcopy(stacks)
            continue
        if not move:
            for i, char_index in enumerate(range(1, 4*stacksN, 4)):
                if line[char_index].isalpha():
                    stacks[i].append(line[char_index])
        if move:
            nums = re.findall(r'\d+', line)
            boxesN, outStack, inStack = map(int, nums)
            for item in stacksPart2[outStack-1][-boxesN:]:
                stacksPart2[inStack-1].append(item)
            for _ in range(boxesN):
                stacksPart2[outStack-1].pop()
            for _ in range(boxesN):
                stacks[inStack-1].append(stacks[outStack-1].pop())
for stack in stacks:
    print(stack[-1], end='')
print()
for stack in stacksPart2:
    print(stack[-1], end='')