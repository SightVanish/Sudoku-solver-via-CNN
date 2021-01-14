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
    b = [[board[i+m][j+n] for m in range(2) for n in range(2) if board[i+m][j+n] != "0"] for i in (0, 2) for j in (0, 2)]
    return all(len(set(x)) == len(x) for x in (*r, *c, *b))

# recursion to find a valid solution (DFS)
def fillRest(order):
    if order == len(empty):
        valid = True
        return valid
    else:
        i, j = empty[order]
        opt = 0b1111 - (row[i] | column[j] | block[i // 2][j // 2])
        while opt:
            num = bin(opt & (-opt)).count('0')   # the rightmost number
            # refresh the record
            row[i] ^= (1 << (num - 1))
            column[j] ^= (1 << (num - 1))
            block[i // 2][j // 2] ^= (1 << (num - 1))
            board[i][j] = str(num)
            # recursion
            valid = fillRest(order + 1)
            # refresh the record again
            row[i] ^= (1 << (num - 1))
            column[j] ^= (1 << (num - 1))
            block[i // 2][j // 2] ^= (1 << (num - 1))
            opt = opt & (opt - 1)   # delete the rightmost
            # pruning
            if valid:
                return valid

# main
# input(preset)
board = [\
    ["0", "4", "0", "0"],\
    ["0", "0", "0", "0"],\
    ["1", "0", "0", "3"],\
    ["0", "0", "0", "1"]]
print("Input:")
for i in range(len(board)):
    print(board[i])

# initialize    
row = [0] * 4
column = [0] * 4
block = [[0] * 2 for _ in range(2)]
for i in range(4):
    for j in range(4):
        if board[i][j] != "0":
            num = int(board[i][j])
            row[i] += 2**(num-1)
            column[j] += 2**(num-1)
            block[i // 2][j // 2] += 2**(num-1)

# fill in grids with only option (DFS)
empty = list()
while True:
    notUpdated = 1
    for i in range(4):
        for j in range(4):
            if board[i][j] == "0":
                opt = 0b1111 - (row[i] | column[j] | block[i // 2][j // 2])
                if bin(opt).count('1') == 1:   # has only option
                    num = int(math.log(opt, 2))
                    # refresh the record
                    row[i] += 2**num
                    column[j] += 2**num
                    block[i // 2][j // 2] += 2**num
                    # fill in the grid
                    board[i][j] = str(num + 1)
                    notUpdated = 0
    if notUpdated:  # cannot update any more
        for i in range(4):
            for j in range(4):
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