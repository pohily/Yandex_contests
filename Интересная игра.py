with open('input.txt', 'r') as f:
    
    data = []
    for line in f:
        data.append(line.strip())
    
    k, n = data[0].split(' ')
    n = int(n)
    k = int(k)
    cards = data[1].split(' ')
    cards = [int(i) for i in cards]
    Vas = 0
    Pet = 0
    
    while True:
        for i in cards:
            if i % 5 == 0:
                Vas += 1
            if i % 3 == 0:
                Pet += 1
            if max(Vas, Pet) == k:
                break
        break
    
    print('k', k, 'Vas', Vas, 'Pet', Pet)
    if Vas > Pet:
        print('Vasya')
    elif Pet > Vas:
        print('Petya')
    else:
        print('Draw')

    
