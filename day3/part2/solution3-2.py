def checkEngineY(i, map, lineCount):
    result = []
    temp2 = i + 1
    if temp2 == len(map[lineCount]):
        temp2 -= 1
    while temp2 > 0 and temp2 > i - 1 and (not map[lineCount][temp2].isdigit()):
        temp2 -= 1
    if not map[lineCount][temp2].isdigit():
        return result
    while temp2 > 0 and map[lineCount][temp2 - 1].isdigit():
        temp2 -= 1
    currNumber = ''
    while temp2 < len(map[lineCount]) and map[lineCount][temp2].isdigit():
        currNumber += map[lineCount][temp2]
        temp2 += 1
    result.append(int(currNumber))
    if i > 0 and not map[lineCount][i].isdigit() and map[lineCount][i - 1].isdigit() and i + 1 < len(map[lineCount]) and map[lineCount][i + 1].isdigit() :
        i -= 1
        currNumber = map[lineCount][i]
        i -=1
        while i >= 0 and map[lineCount][i].isdigit():
            currNumber = map[lineCount][i] + currNumber
            i -= 1
        result.append(int(currNumber))   
    return result

def checkEngine(i, map, lineCount):
    parts = []
    temp = i
    #check right
    if temp <= len(map[lineCount]):
        temp += 1
        if (map[lineCount][temp].isdigit()):
            currNumber = map[lineCount][temp]
            temp += 1
            while temp < len(map[lineCount]) and map[lineCount][temp].isdigit():
                currNumber += map[lineCount][temp]
                temp += 1
            currNumber = int(currNumber)
            print(f"right: {currNumber}")
            parts.append(currNumber)
    #check left
    temp2 = i
    if temp2 > 0:
        temp2 -= 1
        if (map[lineCount][temp2].isdigit()):
            currNumber = map[lineCount][temp2]
            temp2 -= 1
            while temp2 >= 0 and map[lineCount][temp2].isdigit():
                currNumber = map[lineCount][temp2] + currNumber
                temp2 -= 1
            currNumber = int(currNumber)
            print(f"left: {currNumber}")
            parts.append(currNumber)
    #check up
    if lineCount > 0:
        up = checkEngineY(i, map, lineCount - 1)
        if len(up) > 0:
            for upPart in up:
                print(f"up: {upPart}")
                parts.append(upPart)
            if len(parts) > 2:
                return 0
    #check down
    if (lineCount != len(map) - 1):
        down = checkEngineY(i, map, lineCount + 1)
        if len(down) > 0:
            for downPart in down:
                print(f"down: {downPart}")
                parts.append(downPart)
    if len(parts) == 2:
        return parts[0] * parts[1]
    return 0



with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day3/part1/inputD3') as f:
    map = []
    sum = 0
    for line in f:
        map.append(line.strip())

    for lineCount, line in enumerate(map):
        i = 0
        while i < len(line):
            if line[i] == '*':
                print(f"checking line {lineCount}")
                currNumber = checkEngine(i, map, lineCount)
                if currNumber > 0:
                    sum += currNumber
                    print(f"currNumber: {currNumber}")
                    print(map[lineCount])
            i += 1
    print(sum)
            
