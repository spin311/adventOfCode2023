with open('/Users/svits/projects/adventOfCode/adventOfCode2023/day4/part1/inputD4') as f:
    sum = 0
    map = []
    for line in f:
        map.append(line.strip())
    for ticket in map:
        numbers = ticket.split(':')
        win, my = numbers[1].split('|')
        win, my = win.strip().split(" "), my.strip().split(" ")
        winnings = 0
        for num in my:
            if num in win and num != '':
                if winnings == 0:
                    winnings = 1
                else:
                    winnings *= 2
        sum += winnings
    print(sum)
                

        
