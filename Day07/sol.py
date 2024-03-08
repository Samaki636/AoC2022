import re

def part1():
    dirs = get_dirs()
    sum = 0
    for _, dir in dirs.items():
        if dir < 100000:
            sum += dir
    print(sum)

def part2():
    candidates = []
    dirs = get_dirs()
    biggest_dir = int(max(dirs.values()))
    tot_space = 70000000
    free_space = tot_space - biggest_dir
    for _, dir in dirs.items():
        if dir > 30000000 - free_space:
            candidates.append(dir)
    print(min(candidates))

def get_dirs():
    current_path = ""
    dirs = {"/home": 0}
    with open("AoC2022/Day07/input02.txt", 'r') as infile:
        #infile.read() reads all the file and saves it in one String
        #splitlines() splits that String on newline chars and returns a list of strings
        for line in infile.read().splitlines():
            line = line.split()
            if line[0] == "$":
                if line[1] == "ls":
                    pass
                else:
                    if line[2] == "..":
                        current_path = current_path[:current_path.rindex("/")]
                    elif line[2] == "/":
                        current_path = "/home"
                    else:
                        current_path = current_path + "/" + line[2]
                        dirs[current_path] = 0
            else:
                if line[0] != "dir":
                    temp_path = current_path
                    while temp_path != "":
                        dirs[temp_path] += int(line[0])
                        temp_path = temp_path[:temp_path.rindex("/")]
    return dirs

part1()
part2()