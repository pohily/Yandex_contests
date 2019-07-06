result = 0
with open('input.txt', 'r') as f:
    line = f.readline().split(' ')
    for i in line:
        result += int(i)
f = open('output.txt', 'w')
f.write(str(result))
f.close()
