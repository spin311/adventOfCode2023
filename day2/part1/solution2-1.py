colorsLimit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def checkGame(game):
    colors = {
    'red' : 0,
    'green': 0,
    'blue': 0
    }
    stats = game.split(" ")
    for i in range(1, len(stats) - 1, 2):
        color = stats[i + 1].rstrip(',')
        colors[color] = int(stats[i])
        if colors[color] > colorsLimit[color]:
            return False
    return True

with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day2/part1/inputD2') as f:
    sum = 0
    for gameId, line in enumerate(f):
        info = line.split(":")
        games = info[1].split(";")
        valid = True
        for game in games:
            game = game.rstrip('\n')
            if not checkGame(game):
                valid = False
                break
        if valid:
            sum += gameId + 1
    print(sum)

