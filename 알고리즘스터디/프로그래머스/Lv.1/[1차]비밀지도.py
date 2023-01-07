def solution(n, arr1, arr2):
    answer = [""] * n
    solved1 = []
    solved2 = []
    final = []
    
    for number in arr1:
        code = [0] * n
        for i in range(n):
            code[i] = number % 2
            number = number//2
        solved1.append(code[::-1])
    
    for number in arr2:
        code = [0] * n
        for i in range(n):
            code[i] = number % 2
            number = number//2
        solved2.append(code[::-1])
    
    for a in range(n):
        code = []
        number1 = solved1[a]
        number2 = solved2[a]
        for i in range(n):
            if number1[i] != number2[i]:
                code.append(1)
            else:
                code.append(number1[i])
        final.append(code)
        
    for a in range(n):
        for i in range(n):
            if final[a][i]:
                answer[a] += '#'
            else:
                answer[a] += ' '
    return answer