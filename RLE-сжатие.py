def rle(string):
    prev = ''
    count = 0
    result = []
    for char in string:
        if char != prev and count:
            if count > 1:
                result.append(str(count))
            result.append(prev)
            count = 1
            prev = char
        elif char != prev and not count:
            prev = char
            count = 1
        elif char == prev:
            count += 1
    if count > 1:
        result.append(str(count))
    result.append(prev)
    return len(''.join(result))

with open('input.txt', 'r') as f:
    data = []
    for line in f:
        data.append(line.strip())
    s = data[0]
    q = int(data[1])
    querys = []
    for i in range(q):
        querys.append(data[2+i])
    #unzip s
    tmp = []
    times = 1
    for char in s:
        if char.isdigit():
            times = int(char)
        else:
            tmp.append(char*times)
            times = 1
    t = ''.join(tmp)
    # do the q
    result = []
    for query in querys:
        start, end = query.split(' ')
        result.append(rle(t[int(start)-1:int(end)]))
    #output
    for i in result:
        print(i)
