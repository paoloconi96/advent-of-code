UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def rotate(direction):
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    elif direction == LEFT:
        return UP

def puzzle1():
    with open("input-1.txt") as inputFile:
        position = None
        direction = UP
        grid = []
        for line in inputFile:
            grid.append(list(line.rstrip()))
            try:
                i = grid[-1].index("^")
                position = [len(grid) - 1, i]
            except ValueError:
                pass

        result = 0
        while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
            cell = grid[position[0]][position[1]]
            if cell == "#":
                position[0] -= direction[0]
                position[1] -= direction[1]
                direction = rotate(direction)
            elif cell != "X":
                result += 1
                grid[position[0]][position[1]] = "X"

            position[0] += direction[0]
            position[1] += direction[1]

        return result

def test_blocker(grid, r, c, dire, visited):
    if 0 <= r + dire[0] < len(grid) and 0 <= c + dire[1] < len(grid[0]):
        grid[r + dire[0]][c + dire[1]] = "#"

        pr = r
        pc = c
        direction = dire

        while 0 <= pr < len(grid) and 0 <= pc < len(grid[0]):
            visit = (pr, pc, direction)
            if visit in visited:
                return 1

            visited.add(visit)

            cell = grid[pr][pc]
            if cell == "#":
                pr -= direction[0]
                pc -= direction[1]
                direction = rotate(direction)
            else:
                grid[pr][pc] = "U"

            pr += direction[0]
            pc += direction[1]

        return 0
    else:
        return 0

def puzzle2():
    with open("input-1.txt") as inputFile:
        position = None
        direction = UP
        grid = []
        for line in inputFile:
            grid.append(list(line.rstrip()))
            try:
                i = grid[-1].index("^")
                position = [len(grid) - 1, i]
            except ValueError:
                pass

        result = 0
        visited = set()
        while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
            cell = grid[position[0]][position[1]]
            visited.add((position[0], position[1], direction))
            if cell == "#":
                position[0] -= direction[0]
                position[1] -= direction[1]
                direction = rotate(direction)
            elif cell != "X":
                grid[position[0]][position[1]] = "X"
                result += test_blocker([row.copy() for row in grid], position[0], position[1], direction, visited.copy())

            position[0] += direction[0]
            position[1] += direction[1]

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
