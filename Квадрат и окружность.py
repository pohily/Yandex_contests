with open('input.txt', 'r') as f:
    from math import sqrt, pi
    data = []
    coord = []
    for line in f:
        data.append(line.strip())
    n, r = data[0].split(' ')
    r = float(r)
    for d in data[1:]:
        x, y = d.split(' ')
        coord.append((x, y))

    if r > sqrt(2):
        print(len(coord))
    else:
        print(pi*r**2)
