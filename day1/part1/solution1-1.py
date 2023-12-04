def firstNumber(line):
    for char in line:
        if char.isdigit():
            return int(char)

def lastNumber(line):
    for char in line[::-1]:
        if char.isdigit():
            return int(char)


with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day1/part1/inputP1') as file:
    sum = 0
    for line in file:
        firstDigit = firstNumber(line)
        secondDigit = lastNumber(line)
        sum += (firstDigit * 10) + secondDigit
    print(sum)

