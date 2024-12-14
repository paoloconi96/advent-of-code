import math

def puzzle1(rows, cols, secs):
    with open("input-1.txt") as inputFile:
        midRow = rows // 2
        midCol = cols // 2
        quadrants = [0, 0, 0, 0]
        for row in inputFile:
            p, v = row.rstrip().split(" ")
            x, y = [int(n) for n in p[2:].split(",")]
            vx, vy = [int(n) for n in v[2:].split(",")]

            x = x + vx * secs
            x = x % cols

            y = y + vy * secs
            y = y % rows

            if x == midCol or y == midRow:
                continue

            quad = 0
            if x > midCol:
                quad += 1

            if y > midRow:
                quad += 2

            quadrants[quad] += 1

    return math.prod(filter(lambda x: x != 0, quadrants))

def puzzle2(rows, cols, secs):
    with open("input-1.txt") as inputFile:
        cells = []
        filledRow = "111111111111111"
        for row in inputFile:
            p, v = row.rstrip().split(" ")
            x, y = [int(n) for n in p[2:].split(",")]
            vx, vy = [int(n) for n in v[2:].split(",")]

            cells.append((x, y, vx, vy))

        for i in range(secs):
            grid = [[" " for _ in range(cols)] for _ in range(rows)]
            for cell in cells:
                x, y, vx, vy = cell

                x = x + vx * i
                x = x % cols

                y = y + vy * i
                y = y % rows

                grid[y][x] = "1"

            for row in grid:
                row = "".join(row)
                if filledRow in row:
                    return i

    return 0

if __name__ == '__main__':
    print("Result from puzzle 1 is: {}".format(puzzle1(103, 101, 100)))
    print("Result from puzzle 2 is: {}".format(puzzle2(103, 101, 100000)))
