def solution(word):
    answer = 0
    
    nums = ['A','E','I','O','U']
    numbers = []
    for a in nums:
        numbers.append(a)
        for b in nums:
            numbers.append(a+b)
            for c in nums:
                numbers.append(a+b+c)
                for d in nums:
                    numbers.append(a+b+c+d)
                    for e in nums:
                        numbers.append(a+b+c+d+e)
    numbers.sort()
    answer = numbers.index(word) + 1
    return answer