import re

def main():
    matrix = read_file()
    count = len(matrix)*2 + len(matrix[0]*2) - 4
    scenic_scores = []
    for i in range(1, len(matrix)-1) :
        for j in range(1, len(matrix[0])-1):
            if check_tree(i, j, matrix):
                count += 1
                scenic_scores.append(get_scenic_score(i, j, matrix))
    print(count)
    print(max(scenic_scores))

def read_file():
    with open("AoC2022/Day08/input02.txt") as infile:
        file_lines = infile.read().splitlines()
    matrix = []
    for line in file_lines:
        matrix.append([int(x) for x in re.findall(r'\d', line)])
    return matrix

def check_tree(i, j, matrix):
    if (check_tree_left(i, j, matrix) or
        check_tree_right(i, j, matrix) or
        check_tree_top(i, j, matrix) or
        check_tree_bottom(i, j, matrix)):
        return True
    else:
        return False

def check_tree_left(i, j, matrix):
    for k in range(0, j):
        if matrix[i][k] >= matrix[i][j]:
            return False
    else:
        return True
    
def check_tree_right(i, j, matrix):
    for k in range(j+1, len(matrix[0])):
        if matrix[i][k] >= matrix[i][j]:
            return False
    else:
        return True
    
def check_tree_top(i, j, matrix):
    for k in range(0, i):
        if matrix[k][j] >= matrix[i][j]:
            return False
    else:
        return True
    
def check_tree_bottom(i, j, matrix):
    for k in range(i+1, len(matrix)):
        if matrix[k][j] >= matrix[i][j]:
            return False
    else:
        return True
    
def get_scenic_score(i, j, matrix):
    return (get_sc_left(i, j, matrix) * 
            get_sc_right(i, j, matrix) *
            get_sc_top(i, j, matrix) *
            get_sc_bottom(i, j, matrix))

def get_sc_left(i, j, matrix):
    scenic_score = 0
    for k in range(j-1, 0-1, -1):
        scenic_score += 1
        if matrix[i][k] >= matrix[i][j]:
            return scenic_score
    else:
        return scenic_score
    
def get_sc_right(i, j, matrix):
    scenic_score = 0
    for k in range(j+1, len(matrix[0])):
        scenic_score += 1
        if matrix[i][k] >= matrix[i][j]:
            return scenic_score
    else:
        return scenic_score
    
def get_sc_top(i, j, matrix):
    scenic_score = 0
    for k in range(i-1, 0-1, -1):
        scenic_score += 1
        if matrix[k][j] >= matrix[i][j]:
            return scenic_score
    else:
        return scenic_score

def get_sc_bottom(i, j, matrix):
    scenic_score = 0
    for k in range(i+1, len(matrix)):
        scenic_score += 1
        if matrix[k][j] >= matrix[i][j]:
            return scenic_score
    else:
        return scenic_score

main()