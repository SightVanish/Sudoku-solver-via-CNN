# DFS SUDOKU solver
'''
Rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
4. "0" indicates empty cells.
'''
import math

# functions
# check through rules
def isValidSudoku(board):
    r = [[x for x in y if x != "0"] for y in board]
    c = [[x for x in y if x != "0"] for y in zip(*board)]
    b = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != "0"] for i in (0, 3, 6) for j in (0, 3, 6)]
    return all(len(set(x)) == len(x) for x in (*r, *c, *b))

# recursion to find a valid solution (DFS)
def fillRest(order):
    if order == len(empty):
        return 1
    else:
        i, j = empty[order]
        opt = 0b111111111 - (row[i] | column[j] | block[i // 3][j // 3])
        while opt:
            num = bin(opt & (-opt)).count('0')   # the rightmost number
            # refresh the record
            row[i] ^= (1 << (num - 1))
            column[j] ^= (1 << (num - 1))
            block[i // 3][j // 3] ^= (1 << (num - 1))
            board[i][j] = str(num)
            # recursion
            valid = fillRest(order + 1)
            # refresh the record again
            row[i] ^= (1 << (num - 1))
            column[j] ^= (1 << (num - 1))
            block[i // 3][j // 3] ^= (1 << (num - 1))
            opt = opt & (opt - 1)   # delete the rightmost
            # pruning
            if valid:
                return 1

# main
# input(preset)
board = [\
    ["5","3","0","0","7","0","0","0","0"],\
    ["6","0","0","1","9","5","0","0","0"],\
    ["0","9","8","0","0","0","0","6","0"],\
    ["8","0","0","0","6","0","0","0","3"],\
    ["4","0","0","8","0","3","0","0","1"],\
    ["0","0","0","0","2","0","0","0","6"],\
    ["0","6","0","0","0","0","2","8","0"],\
    ["0","0","0","4","1","9","0","0","5"],\
    ["0","0","0","0","8","0","0","7","9"]]
print("Input:")
for i in range(len(board)):
    print(board[i])

# initialize    
row = [0] * 9
column = [0] * 9
block = [[0] * 3 for _ in range(3)]
for i in range(9):
    for j in range(9):
        if board[i][j] != "0":
            num = int(board[i][j])
            row[i] += 2**(num-1)
            column[j] += 2**(num-1)
            block[i // 3][j // 3] += 2**(num-1)

# fill in grids with only option (DFS)
empty = list()
while True:
    notUpdated = 1
    for i in range(9):
        for j in range(9):
            if board[i][j] == "0":
                opt = 0b111111111 - (row[i] | column[j] | block[i // 3][j // 3])
                if bin(opt).count('1') == 1:   # has only option
                    num = int(math.log(opt, 2))
                    # refresh the record
                    row[i] += 2**num
                    column[j] += 2**num
                    block[i // 3][j // 3] += 2**num
                    # fill in the grid
                    board[i][j] = str(num + 1)
                    notUpdated = 0
    if notUpdated:  # cannot update any more
        for i in range(9):
            for j in range(9):
                if board[i][j] == "0":
                    empty.append((i, j))
        break

# recursion to find a valid solution (DFS)
fillRest(0)

# output
print("Output:")
if isValidSudoku(board):
    for i in range(len(board)):
        print(board[i])
else:
    print("False")