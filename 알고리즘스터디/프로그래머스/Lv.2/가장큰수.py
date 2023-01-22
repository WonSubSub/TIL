def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: (x[0%len(x)], x[1%len(x)], x[2%len(x)], x[3%len(x)]))
    
    answer = str(int(''.join(numbers[::-1])))
    
    return answer