def recCards(map, currCard):
    if currCard >= len(map):
        return 0
    card = map[currCard]
    numbers = card.split(":")
    win, my = numbers[1].split('|')
    win, my = win.strip().split(" "), my.strip().split(" ")
    count = 0
    for num in my:
        if num in win and num != '':
            count += 1
    sum = 0
    for i in range(count):
        sum += 1 + recCards(map, currCard + i + 1)
    return sum

    

    


with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day4/part1/inputD4') as f:
    sum = 0
    map = []
    for line in f:
        map.append(line.strip())
    for i, ticket in enumerate(map):
        lineCards = recCards(map, i)
        sum += lineCards + 1
    print(sum)
                

        
