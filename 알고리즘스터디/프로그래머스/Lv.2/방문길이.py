def solution(dirs):
    answer = 0
    lengths = []
    current = [0,0]
    nex = [0,0]
    for d in dirs:
        if d == "L":
            nex = [current[0]-1, current[1]]
            if -5 <= current[0]-1 <= 5 and -5 <= current[1] <= 5:
                b = sorted([current,nex])
                lengths.append(b)
                current = nex
        if d == "D":
            nex = [current[0], current[1]-1]
            if -5 <= current[0] <= 5 and -5 <= current[1]-1 <= 5:
                b = sorted([current,nex])
                lengths.append(b)
                current = nex
        if d == "R":
            nex = [current[0]+1, current[1]]
            if -5 <= current[0]+1 <= 5 and -5 <= current[1] <= 5:
                b = sorted([current,nex])
                lengths.append(b)
                current = nex
        if d == "U":
            nex = [current[0], current[1]+1]
            if -5 <= current[0] <= 5 and -5 <= current[1]+1 <= 5:
                b = sorted([current,nex])
                lengths.append(b)
                current = nex
    ans_check = []
    for i in lengths:
        if i not in ans_check:
            ans_check.append(i)
    answer = len(ans_check)
    return answer
