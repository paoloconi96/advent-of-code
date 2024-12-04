from collections import deque, defaultdict

xmas = ["X", "M", "A", "S"]
xmas_rev = ["S", "A", "M", "X"]
def get_diagonal(grid, x, y, dir_x, dir_y, word_len):
    diag = []
    for i in range(word_len):
        diag.append(grid[y][x])
        x += dir_x
        y += dir_y

    return diag

def puzzle1():
    with open("input-1.txt") as inputFile:
        grid = [list(line.rstrip()) for line in inputFile]
        result = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # Horizontal
                if x >= 3 and grid[y][x-3:x+1] == xmas_rev:
                    result += 1
                if x + 3 < len(grid[0]) and grid[y][x:x+4] == xmas:
                    result += 1

                # Vertical
                if y >= 3 and [grid[k][x] for k in range(y - 3, y + 1)] == xmas_rev:
                    result += 1
                if y + 3 < len(grid) and [grid[k][x] for k in range(y, y + 4)] == xmas:
                    result += 1

                # Diagonal
                if x >= 3 and y >= 3 and get_diagonal(grid, x, y, -1, -1, len(xmas)) == xmas:
                    result += 1
                if x + 3 < len(grid[0]) and y >= 3 and get_diagonal(grid, x, y, 1, -1, len(xmas)) == xmas:
                    result += 1
                if x + 3 < len(grid[0]) and y + 3 < len(grid) and get_diagonal(grid, x, y, 1, 1, len(xmas)) == xmas:
                    result += 1
                if x >= 3 and y + 3 < len(grid) and get_diagonal(grid, x, y, -1, 1, len(xmas)) == xmas:
                    result += 1

        return result

mas = ["M", "A", "S"]
def puzzle2():
    with open("input-1.txt") as inputFile:
        grid = [list(line.rstrip()) for line in inputFile]
        result = 0
        diags = defaultdict(int)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if x >= len(mas) - 1 and y >= len(mas) - 1 and get_diagonal(grid, x, y, -1, -1, len(mas)) == mas:
                    diags[(x - 1, y - 1)] += 1
                if x + len(mas) - 1 < len(grid[0]) and y >= len(mas) - 1 and get_diagonal(grid, x, y, 1, -1, len(mas)) == mas:
                    diags[(x + 1, y - 1)] += 1
                if x + len(mas) - 1 < len(grid[0]) and y + len(mas) - 1 < len(grid) and get_diagonal(grid, x, y, 1, 1, len(mas)) == mas:
                    diags[(x + 1, y + 1)] += 1
                if x >= len(mas) - 1 and y + len(mas) - 1 < len(grid) and get_diagonal(grid, x, y, -1, 1, len(mas)) == mas:
                    diags[(x - 1, y + 1)] += 1

        for n in diags:
            if diags[n] > 1:
                result += 1

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
