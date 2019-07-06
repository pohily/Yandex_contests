def pow_2(num):
    while num // 2 > 1:
        if num % 2 != 0:
            return False
        else:
            num //= 2
    
    return True if num == 2 else False
    
with open('input.txt', 'r') as f:
    from collections import defaultdict
    data = []
    for line in f:
        data.append(line.strip())
    
    pairs = defaultdict(int)
    players = set()
    for game in data[1:]:
        x, y = game.split(' ')
        players.add(x)
        players.add(y)
        pairs[x] += 1
        pairs[y] += 1

    n = len(players)
    if not pow_2(n): # не степень двойки
        print('NO SOLUTION')
    else:
        max_played = 0
        final = []
        for i in pairs.items():
            a, s = i
            if s == max_played:
                final.append(a)
            elif s > max_played:
                max_played = s
                final = []
                final.append(a)
        for i in final:
            print(i, end=' ')
