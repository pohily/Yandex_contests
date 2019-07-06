import sys
commits = sys.stdin.readline().strip()
commits = int(commits)

# попробуем бинарный поиск
end = commits
start = 0
rest = 25

while True:
    if end - start <= rest:
        print(start, end='\n', file=sys.stdout, flush=True)
        
        rest -= 1
        answer = sys.stdin.readline().strip()
        answer = int(answer)
        if answer == 0:
            print('! ', start, end='\n', file=sys.stdout, flush=True)
            break
        start += 1
    else:
        newstart = start + (end - start) // 2
        print(newstart, end='\n', file=sys.stdout, flush=True)
        
        rest -= 1
        answer = sys.stdin.readline().strip()
        answer = int(answer)
        if answer == 0:
            end = newstart
        else:
            start = newstart


