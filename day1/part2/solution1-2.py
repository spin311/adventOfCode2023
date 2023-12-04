wordsToNumbers = {
    'one': 1,
    'two': 2,
    'three': 3, 
    'four': 4,
    'five': 5,
    'six': 6, 
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def firstNumber(line):
    word = ''
    for char in line:
        if char.isdigit():
            return int(char)
        word += char
        for key in wordsToNumbers:
            if key in word:
                return wordsToNumbers[key]

def lastNumber(line):
    word = ''
    for char in line[::-1]:
        if char.isdigit():
            return int(char)
        word = char + word
        for key in wordsToNumbers:
            if key in word:
                return wordsToNumbers[key]
        
with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day1/part1/inputP1') as file:
    sum = 0
    for line in file:
        firstDigit = firstNumber(line)
        secondDigit = lastNumber(line)
        sum += (firstDigit * 10) + secondDigit
    print(sum)

