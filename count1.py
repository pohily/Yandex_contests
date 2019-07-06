arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(int(line))
        
start = 0
best = 0
print(arr)
for i in arr:
    if i == 1:
        start +=1
        best = max(start, best)
    else:
        start = 0
print(best)
