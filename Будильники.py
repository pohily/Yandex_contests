with open('input.txt', 'r') as f:
    
    data = []
    for line in f:
        data.append(line.strip())
    
    n, x, k = data[0].split(' ')
    n = int(n)
    x = int(x)
    k = int(k)
    t = data[1].split(' ')
    t = sorted([int(i) for i in t])
    
    alarms = []
    next_alarm = {}
    max_t = max(t)

    for alarm in t:
        time = 0
        while alarm + time <= max_t:
            if alarm + time not in alarms:
                alarms.append(alarm + time)
                alarms.sort()
            time += x
        next_alarm[alarm] = time

    if len(alarms) >= k:
        print(alarms)
        print(alarms[k-1])

    #if every alarm maxed to max_t and it's not enough
    while len(alarms) < k:
        for alarm in t:
            if alarm + next_alarm[alarm] not in alarms:
                alarms.append(alarm + next_alarm[alarm])
                next_alarm[alarm] += x
            alarms.sort()
    print(alarms)
    print(alarms[k-1])

        


   
            
            
