def parseButton(line):
    valuesLine = line[12:]
    valuesSplitted = valuesLine.split(", ")

    return int(valuesSplitted[0]), int(valuesSplitted[1][2:])

def puzzle1():
    result = 0
    with open("input-1.txt") as inputFile:
        lines = list(reversed(inputFile.readlines()))

    while lines:
        aLine = lines.pop().rstrip()
        ax, ay = parseButton(aLine)

        bLine = lines.pop().rstrip()
        bx, by = parseButton(bLine)

        prizeLine = lines.pop().rstrip()
        valuesLine = prizeLine[9:]
        valuesSplitted = valuesLine.split(", ")
        px, py = int(valuesSplitted[0]), int(valuesSplitted[1][2:])

        best = 1000
        for aPress in range(1, 101):
            for bPress in range(1, 101):
                if px - (ax * aPress + bx * bPress) == 0 and py - (ay * aPress + by * bPress) == 0:
                    best = min(best, aPress * 3 + bPress)

        if best != 1000:
            result += best

        if lines:
            lines.pop()

    return result

def puzzle2():
    result = 0
    with open("input-1.txt") as inputFile:
        lines = list(reversed(inputFile.readlines()))

    while lines:
        aLine = lines.pop().rstrip()
        ax, ay = parseButton(aLine)

        bLine = lines.pop().rstrip()
        bx, by = parseButton(bLine)

        prizeLine = lines.pop().rstrip()
        valuesLine = prizeLine[9:]
        valuesSplitted = valuesLine.split(", ")
        px, py = int(valuesSplitted[0]) + 10000000000000, int(valuesSplitted[1][2:]) + 10000000000000

        aPress, remA = divmod(px * by - py * bx, ax * by - ay * bx)
        bPress, remB = divmod(py * ax - px * ay, ax * by - ay * bx)
        if remA == remB == 0:
            result += 3 * aPress + bPress

        if lines:
            lines.pop()

    return result

if __name__ == '__main__':
    print("Result from puzzle 1 is: {}".format(puzzle1()))
    print("Result from puzzle 2 is: {}".format(puzzle2()))
