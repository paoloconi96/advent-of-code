from collections import deque
from functools import cmp_to_key


def puzzle1():
    with open("input-1.txt") as inputFile:
        grid = [list(l.rstrip()) for l in inputFile]

    result = 0
    visitedIslands = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in visitedIslands:
                continue

            letter = grid[row][col]
            queue = deque([(row, col)])
            visited = set()

            perimeter = 0
            area = 0
            while queue:
                cRow, cCol = queue.popleft()
                if (cRow, cCol) in visited:
                    if grid[cRow][cCol] != letter:
                        perimeter += 1
                    continue

                if cRow < 0 or cRow >= len(grid) or cCol < 0 or cCol >= len(grid[0]):
                    perimeter += 1
                    continue

                if grid[cRow][cCol] != letter:
                    perimeter += 1
                    continue

                area += 1
                visited.add((cRow, cCol))
                visitedIslands.add((cRow, cCol))

                queue.append((cRow + 1, cCol))
                queue.append((cRow, cCol + 1))
                queue.append((cRow - 1, cCol))
                queue.append((cRow, cCol - 1))

            result += perimeter * area

    return result

def puzzle2():
    with open("input-1.txt") as inputFile:
        grid = [list(l.rstrip()) for l in inputFile]

    result = 0
    visitedIslands = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in visitedIslands:
                continue

            letter = grid[row][col]
            queue = deque([(0, row, col)])
            visited = set()

            perimeter = list()
            area = 0
            while queue:
                direction, cRow, cCol = queue.popleft()
                if (cRow, cCol) in visited:
                    if grid[cRow][cCol] != letter:
                        perimeter.append((direction, cRow, cCol))
                    continue

                if cRow < 0 or cRow >= len(grid) or cCol < 0 or cCol >= len(grid[0]):
                    perimeter.append((direction, cRow, cCol))
                    continue

                if grid[cRow][cCol] != letter:
                    perimeter.append((direction, cRow, cCol))
                    continue

                area += 1
                visited.add((cRow, cCol))
                visitedIslands.add((cRow, cCol))

                queue.append((0, cRow - 1, cCol))
                queue.append((1, cRow, cCol + 1))
                queue.append((2, cRow + 1, cCol))
                queue.append((3, cRow, cCol - 1))

            sides = len(perimeter)

            perimeter.sort()
            for i in range(1, len(perimeter)):
                cDir, cRow, cCol = perimeter[i]
                pDir, pRow, pCol = perimeter[i - 1]

                if cDir != pDir:
                    continue

                if cRow == pRow and cCol == pCol + 1:
                    sides -= 1

            perimeter.sort(key=lambda x: (x[0], x[2], x[1]))
            for i in range(1, len(perimeter)):
                cDir, cRow, cCol = perimeter[i]
                pDir, pRow, pCol = perimeter[i - 1]

                if cDir != pDir:
                    continue

                if cCol == pCol and cRow == pRow + 1:
                    sides -= 1

            result += sides * area

    return result

if __name__ == '__main__':
    print("Result from puzzle 1 is: {}".format(puzzle1()))
    print("Result from puzzle 2 is: {}".format(puzzle2()))
