with open('input.txt', 'r') as f:
    import re
    data = []
    for line in f:
        data.append(line.strip())
    
    x = int(data[0])
    t = int(data[1])
    prog = []
    
    for i in data[2:]:
        prog.append(i)
    prog = ''.join(prog)

    names = []
    excs = []
    f = {} # func text
    funcs = prog.split('func ')
    for i in funcs:
        if i:
            name = i[:i.index('(')]
            names.append(name)
            f[name] = i[i.index(')')+1:]
    
    #try - suppress 
    for i, v in f.items():
        result = re.search(r'try', v)
        start = result.start
        result = re.search(r'suppress', v)
        end = result.end

    #finally
    for i in f.keys():
        for ind, value in f.items():
            if i in value:
                f[ind] = value.replace(i, f[i])
    print(start, end)

