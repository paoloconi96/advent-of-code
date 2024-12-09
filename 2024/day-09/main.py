from collections import defaultdict, deque


def puzzle1():
    with open("input-1.txt") as inputFile:
        disk = list(inputFile.read().rstrip())
        diskExpanded = []

        fileId = 0
        isFile = True
        for p in disk:
            if isFile:
                diskExpanded.extend([fileId] * int(p))
                fileId += 1
            else:
                diskExpanded.extend(['.'] * int(p))

            isFile = not isFile

        p1 = 0
        result = 0
        while p1 < len(diskExpanded):
            if diskExpanded[p1] != ".":
                result += diskExpanded[p1] * p1
                p1 += 1
                continue

            if diskExpanded[-1] == ".":
                diskExpanded.pop()
                continue

            diskExpanded[p1] = diskExpanded.pop()
            result += diskExpanded[p1] * p1
            p1 += 1

        return result

def puzzle2():
    with open("input-1.txt") as inputFile:
        disk = list(inputFile.read().rstrip())

    avais = []
    fileId = 0
    isFile = True
    for p in disk:
        if isFile:
            avais.append((int(p), fileId))
            fileId += 1
        isFile = not isFile

    result = 0
    i = 0

    fileId = 0

    used = set()
    isFile = True
    for p in disk:
        length = int(p)
        if isFile:
            if fileId not in used:
                result += sum(fileId * n for n in range(i, i + length))
                used.add(fileId)
            i += length
            fileId += 1
        else:
            for j in range(len(avais) - 1, -1, -1):
                a = avais[j]
                if a[0] <= length and a[1] not in used:
                    result += sum(a[1] * n for n in range(i, i + a[0]))
                    used.add(a[1])
                    i += a[0]
                    length -= a[0]
                    if length == 0:
                        break

            i += length


        isFile = not isFile

    return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
