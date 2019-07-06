with open('input.txt', 'r') as f:
    data = []
    for line in f:
        data.append(line.strip())
    tels = []
    formats = []
    t = int(data[0])+1
    for i in range(1, t):
        tels.append(data[i])
    for i in range(t+1, int(data[t])+1+t):
        formats.append(data[i])
    
    # format tels
    for i, t in enumerate(tels):
        tmp = t
        tmp = tmp.replace('-', '')
        tmp = tmp.replace(' ', '')
        tmp = tmp.replace('(', '')
        tmp = tmp.replace(')', '')
        if tmp[0] != '+':
            tels[i] = '+' + tmp
        else:
            tels[i] = tmp
    
    
    # format formats
    form = []
    digits = []
    names = []
    for f in formats:
        p = f.index('-')
        tmp = []
        for char in f:
            if char.isdigit() or char == '+':
                tmp.append(char)
            elif char in [' ', '(', ')']:
                
                continue
            else:
                form.append(''.join(tmp))
                digits.append(f[:p].count('X'))
                names.append(f[p:])
                break
    # check
    result = []
    for t in tels:
        for i, f in enumerate(form):
            if t.startswith(f) and len(t) == len(f) + digits[i]:
                result.append(formats[i][:formats[i].index('X')]+t[-digits[i]:]+' '+names[i])

    for i in result:
        print(i)
    
 
