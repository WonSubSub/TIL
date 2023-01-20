def solution(elements):
    answer = 0
    
    elements.extend(elements)
    sums = set()
    
    for i in range(1,len(elements)//2+1):
        temp_sum = sum(elements[:i])
        for a in range(len(elements)-i):
            temp_sum -= elements[a]
            temp_sum += elements[a+i]
            sums.add(temp_sum)
    answer = len(sums)
    return answer