def perfect_shuffle(deck):
    velkost = len(deck)
    part1 = deck[:velkost//2]
    part2 = deck[velkost//2:]
    # print(part1, part2)

    result = [ ]
    for i in range(velkost//2):
        result.append(part1[i])
        result.append(part2[i])
    
    return result