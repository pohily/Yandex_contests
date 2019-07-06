with open('input.txt', 'r') as f:
    from itertools import permutations
    from functools import reduce
    data = []
    for line in f:
        data.append(line.strip())

    tmp = data[0].split(' ')
    tmp = [int(i) for i in tmp]
    n, m, k = tmp
    tmp = data[1].split(' ')
    a = [int(i) for i in tmp]

    for i in permutations(a, k):
        
        p = reduce(lambda x, y: x*y, i)
        if p == m:
            used = []
            for j in i:
                ind = a.index(j)
                used.append(str(ind+1))
                a[ind] = ''
            break
    print(' '.join(used))


