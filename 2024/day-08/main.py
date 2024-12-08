from collections import defaultdict

def puzzle1():
    with open("input-1.txt") as inputFile:
        antennas = defaultdict(list)
        rowLen = 0
        colLen = 0
        for line in inputFile:
            colLen = len(line)
            for j in range(len(line) - 1):
                if line[j] == ".":
                    continue

                antennas[line[j]].append((rowLen, j))

            rowLen += 1

        result = set()
        for poss in antennas.values():
            for i in range(len(poss)):
                row1, col1 = poss[i]
                for j in range(i+1, len(poss)):
                    row2, col2 = poss[j]
                    row, col = row2 - row1, col2 - col1

                    arow, acol = row1 - row, col1 - col
                    if 0 <= arow < rowLen and 0 <= acol < colLen:
                        result.add((arow, acol))

                    arow, acol = row2 + row, col2 + col
                    if 0 <= arow < rowLen and 0 <= acol < colLen:
                        result.add((arow, acol))

        return len(result)

def puzzle2():
    with open("input-1.txt") as inputFile:
        antennas = defaultdict(list)
        rowLen = 0
        colLen = 0
        for line in inputFile:
            colLen = len(line)
            for j in range(len(line) - 1):
                if line[j] == ".":
                    continue

                antennas[line[j]].append((rowLen, j))

            rowLen += 1

        result = set()
        for poss in antennas.values():
            for i in range(len(poss)):
                row1, col1 = poss[i]
                for j in range(i+1, len(poss)):
                    row2, col2 = poss[j]
                    row, col = row2 - row1, col2 - col1

                    arow, acol = row1, col1
                    while 0 <= arow < rowLen and 0 <= acol < colLen:
                        result.add((arow, acol))
                        arow, acol = arow - row, acol - col

                    arow, acol = row2, col2
                    while 0 <= arow < rowLen and 0 <= acol < colLen:
                        result.add((arow, acol))
                        arow, acol = arow + row, acol + col

        return len(result)

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
