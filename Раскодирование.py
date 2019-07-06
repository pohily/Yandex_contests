with open('input.txt', 'r') as f:
    from re import findall
    data = []
    for line in f:
        data.append(line.strip())
    
    line = data[0]
    count = 0
    
    while True:
        result = findall(r'~[abcdefABCDEF0123456789][abcdefABCDEF0123456789]', line)
        if not result:
            break
        for sub in result:
            x = sub[1]
            y = sub[2]
            replace = 16 * int(x, 16) + int(y, 16)
            line = line.replace(sub, chr(replace))
        count += 1
        if '~' not in line and len(line) < 3:
            break
    print(count)
