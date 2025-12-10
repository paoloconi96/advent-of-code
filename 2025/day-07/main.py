import pprint
import re
from collections import defaultdict
from functools import reduce


def puzzle1():
    with (open("input-1.txt") as inputFile):
        grid = [list(line.rstrip()) for line in inputFile]
        col = grid[0].index("S")
        stack = [(1, col)]
        visited = set()
        result = 0
        while stack:
            el = stack.pop()
            row, col = el
            if col < 0 or row == len(grid) or col == len(grid[0]):
                continue

            if el in visited:
                continue

            if grid[row][col] == "^":
                result += 1
                stack.append((row, col - 1))
                stack.append((row, col + 1))
            else:
                stack.append((row + 1, col))

            visited.add(el)

        return result

def puzzle2():
    with (open("input-1.txt") as inputFile):
        grid = [list(line.rstrip()) for line in inputFile]
        col = grid[0].index("S")
        return follow_path(grid, 1, col, {})

def follow_path(grid, row, col, memo):
    if row == len(grid):
        return 1

    key = str(row) + "," + str(col)
    if key in memo:
        return memo[key]

    if grid[row][col] == "^":
        memo[key] = follow_path(grid, row, col-1, memo) + follow_path(grid, row, col+1, memo)
    else:
        memo[key] = follow_path(grid, row+1, col, memo)

    return memo[key]

if __name__ == '__main__':
    print("Puzzle 1: {}".format(puzzle1()))
    print("Puzzle 2: {}".format(puzzle2()))
