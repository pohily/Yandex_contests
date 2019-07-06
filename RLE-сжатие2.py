def pos(ind, string):
    count = 0
    ind = int(ind) 
    for i, char in enumerate(string):
        if char.isalpha():
            count += 1
        else:
            count += int(char)-1
        if char.isalpha() and count >= ind:
            break
    return ind
    

with open('input.txt', 'r') as f:
    data = []
    for line in f:
        data.append(line.strip())
    s = data[0]
    q = int(data[1])
    querys = []
    for i in range(q):
        querys.append(data[2+i])

    # list from s
    letter = []
    tmp = s
    num = ''
    for i in tmp:
        if i.isalpha():
            if num:
                letter.append(num)
                num = ''
            letter.append(i)
        else:
            num += i
    
    # do the q
    result = []
    for query in querys:
        start, end = query.split(' ')
        result.append(pos(end, letter) - pos(start, letter))
    #output
    for i in result:
        print(i)
