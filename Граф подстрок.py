with open('input.txt', 'r') as f:
    from collections import defaultdict
    data = []
    for line in f:
        data.append(line.strip())

    
    #find words
    words = []
    ver = []
    for i in data[1:]:
        words.append([])
        for j in range(3, len(i)+1):
            words[-1].append(i[j-3:j])
            ver.append(i[j-3:j])

    # vertices 
    ver = set(ver)
    print(len(ver))

    #graph
    d = defaultdict(int)
    for w in words:
        for ind, word in enumerate(w[:-1]):
            d[word, w[ind+1]] += 1
    d = sorted(d.items())
    edge = len(d)
    

    #edges
    print(edge)

    for i in d:
        a, s = i
        d, f = a
        print(d, f, s)
    
