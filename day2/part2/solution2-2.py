colorsLimit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def checkGame(game):
    colorsGame = {
    'red' : 0,
    'green': 0,
    'blue': 0
    }
    stats = game.split(" ")
    for i in range(1, len(stats) - 1, 2):
        color = stats[i + 1].rstrip(',')
        currCubes = int(stats[i])
        if (colorsGame[color] < currCubes):
            colorsGame[color] = int(stats[i])
    return colorsGame

with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day2/part1/inputD2') as f:
    sum = 0
    for line in f:
        info = line.split(":")
        gameId = int(info[0].split(" ")[1])
        games = info[1].split(";")
        colorsSum = {
        'red' : 0,
        'green': 0,
        'blue': 0
        }        
        for game in games:
            game = game.rstrip('\n')
            currColors = checkGame(game)
            for key in colorsSum:
                if colorsSum[key] < currColors[key]:
                    colorsSum[key] = currColors[key]
        sum += colorsSum['red'] * colorsSum['green'] * colorsSum['blue']
        
    print(sum)

