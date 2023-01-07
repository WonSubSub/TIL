def solution(sizes):
    answer = 0
    a = []
    b = []
    for size in sizes:
        size.sort()
        a.append(size[0])
        b.append(size[1])
            
    answer = max(a) * max(b)
        
    return answer