def checkYTiles(numLen, temp, map, lineCount):
    char = temp - 1
    while char <= temp + numLen:
        if char < 0 or char >= len(map[lineCount]):
            char += 1
            continue
        currChar = map[lineCount][char]
        if ((not currChar.isdigit()) and currChar != '.'):
            return True
        char += 1
    return False


def checkTiles(numLen, temp, map, lineCount):
    if (temp != 0 and map[lineCount][temp - 1] != '.'):
        return True
    if (temp + numLen < len(map[lineCount]) and map[lineCount][temp + numLen] != '.'):
        return True
    if (lineCount != 0 and checkYTiles(numLen, temp, map, lineCount - 1)):
        return True    
    if (lineCount != len(map) - 1 and checkYTiles(numLen, temp, map, lineCount + 1)):
        return True
    return False

with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day3/part1/inputD3') as f:
    map = []
    sum = 0
    for line in f:
        map.append(line.strip())

    for lineCount, line in enumerate(map):
        i = 0
        while i < len(line):
            char = line[i]
            if char.isdigit():
                temp = i
                currNumber = ''
                while i < len(line) and line[i].isdigit():
                    currNumber += line[i]
                    i += 1
                numLen = len(currNumber)
                currNumber = int(currNumber)
                if checkTiles(numLen, temp, map, lineCount):
                    print(f"currNumber: {currNumber}")
                    sum += currNumber
                    print(f"sum: {sum}")
            i += 1
    print(sum)
            
