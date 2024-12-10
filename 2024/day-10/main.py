DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def countTrails(grid, i, j, part2):
    stack = [(i, j, -1)]
    paths = 0
    visited = set()
    while stack:
        row, col, prev = stack.pop()
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            value = grid[row][col]
            if prev + 1 != value:
                continue

            if (row, col) in visited and not part2:
                continue

            if value == 9:
                paths += 1
                visited.add((row, col))

            for drow, dcol in DIRECTIONS:
                stack.append((row + drow, col + dcol, value))

    return paths

def puzzle1():
    with open("input-1.txt") as inputFile:
        grid = []
        for i in inputFile:
            grid.append([int(n) for n in i.rstrip()])

    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cv = grid[row][col]
            if cv == 0:
                result += countTrails(grid, row, col, False)

    return result

def puzzle2():
    with open("input-1.txt") as inputFile:
        grid = []
        for i in inputFile:
            grid.append([int(n) for n in i.rstrip()])

    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cv = grid[row][col]
            if cv == 0:
                result += countTrails(grid, row, col, True)

    return result

if __name__ == '__main__':
    print("Result from puzzle 1 is: {}".format(puzzle1()))
    print("Result from puzzle 2 is: {}".format(puzzle2()))
