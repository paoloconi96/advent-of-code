def parse_mul(op):
    commaI = op.find(",")
    closingI = op.find(")")
    if commaI == -1 or closingI == -1:
        return 0

    try:
        first = int(op[:commaI])
        second = int(op[commaI + 1:closingI])
    except ValueError:
        return 0

    return first * second

def puzzle1():
    with open("input-1.txt") as inputFile:
        memory = inputFile.read(-1).replace("\n", "")
        ops = memory.split("mul(")
        return sum([parse_mul(op) for op in ops])

def puzzle2():
    with open("input-1.txt") as inputFile:
        memory = inputFile.read(-1).replace("\n", "")

        dontops = []
        for dont in memory.split("don't()"):
            dontops.append(dont)
            dontops.append("dont")
        dontops.pop()

        doops = []
        for op in dontops:
            if op.find("do()") != -1:
                for do in op.split("do()"):
                    doops.append(do)
                    doops.append("do")
            else:
                doops.append(op)
        doops.pop()

        ops = []
        for op in doops:
            if op.find("mul(") != -1:
                for mul in op.split("mul("):
                    res = parse_mul(mul)
                    if res != 0:
                        ops.append(res)
            else:
                ops.append(op)

        result = 0
        enabled = True
        for op in ops:
            if op == "dont":
                enabled = False
            elif op == "do":
                enabled = True
            elif enabled:
                result += op

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
