def checkTiles(currNumber, numLen, i, map, lineCount):
    if(map[lineCount][] != '.'):
        return True
    else:




with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day3/part1/inputD3') as f:
    map = []
    sum = 0
    for line in f:
        map.append(line)
    print(len(map))
    for lineCount, line in enumerate(map):
        i = 0
        while i < len(line):
            char = line[i]
            if char.isdigit():
                currNumber = ''
                while char.isdigit():
                    currNumber += char
                    i += 1
                    char = line[i]
                numLen = len(currNumber)
                currNumber = int(currNumber)
                if checkTiles(currNumber, numLen, i, map, lineCount):
                    sum+= currNumber
            i += 1
            
