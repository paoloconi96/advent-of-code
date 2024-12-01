from collections import defaultdict


def puzzle1():
    with open("input-1.txt") as inputFile:
        list1 = []
        list2 = []

        while True:
            line = inputFile.readline()
            if line == '':
                break

            el1, el2 = line.strip().split("   ")
            list1.append(int(el1))
            list2.append(int(el2))

        list1.sort()
        list2.sort()

        distance = 0
        for i in range(len(list1)):
            distance += abs(list1[i] - list2[i])

        return distance

def puzzle2():
    with open("input-1.txt") as inputFile:
        list1 = []
        map2 = defaultdict(int)

        while True:
            line = inputFile.readline()
            if line == '':
                break

            el1, el2 = line.strip().split("   ")
            list1.append(int(el1))
            map2[int(el2)] += 1

        list1.sort()

        similarity = 0
        for el in list1:
            similarity += el * map2[el]

        return similarity

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
