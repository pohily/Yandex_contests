with open('input.txt', 'r') as f:
    data = []
    for line in f:
        data.append(line.strip())
    result = 0  
     
    #/6
    num = list(data[0])
    len_num = len(num) 
    sum_num = sum([int(i) for i in num])
    if sum_num % 3 == 0:
        two = num.count('2')
        if two:
            result += num.count('2') / len_num  
    #/5
    five = num.count('5')
    if five:
        result += num.count('5') / len_num

    print(result)
