def check_report_validity(report):
    direction = 'up' if report[0] < report[1] else 'down'
    current_valid = True
    for i in range(1, len(report)):
        num1, num2 = report[i], report[i - 1]
        diff = abs(num1 - num2)
        if (direction == 'up' and num1 < num2) or (direction == 'down' and num1 > num2) or (diff < 1 or diff > 3):
            current_valid = False
            break

    return current_valid

def puzzle1():
    with open("input-1.txt") as inputFile:
        valid = 0
        while True:
            line = inputFile.readline()
            if line == '':
                break

            numbers = [int(n) for n in line.strip().split()]
            current_valid = check_report_validity(numbers)

            if current_valid:
                valid += 1

        return valid

def puzzle2():
    with open("input-1.txt") as inputFile:
        valid = 0
        while True:
            line = inputFile.readline()
            if line == '':
                break

            numbers = [int(n) for n in line.strip().split()]
            if check_report_validity(numbers):
                valid += 1
                continue

            for i in range(len(numbers)):
                ns = numbers[:]
                del ns[i]
                if check_report_validity(ns):
                    valid += 1
                    break

        return valid

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
