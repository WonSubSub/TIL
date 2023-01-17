def solution(dartResult):
    answer = 0
    alphabet = ['S', 'D', 'T']
    shape = ['*', '#']
    nums = []
    alphas = []
    shapes = []
    num_cnt = 0
    n = ''
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            n += dartResult[i]
        elif dartResult[i] in alphabet:
            nums.append(int(n))
            n = ''
            num_cnt += 1
            alphas.append(dartResult[i])
            if i != len(dartResult) -1:
                if dartResult[i+1] in shape:
                    shapes.append(dartResult[i+1])
                else:
                    shapes.append(1)
    if len(shapes) == 2:
        shapes.append(1)
    
    for i in range(3):
        nums[i] = nums[i]**(alphabet.index(alphas[i])+1)
    
    for i in range(3):
        if shapes[i] == '#':
            nums[i] = nums[i] * -1
        elif shapes[i] == '*':
            if i != 0:
                nums[i] = nums[i] * 2
                nums[i-1] = nums[i-1] * 2
            else:
                nums[i] = nums[i] * 2
    answer = sum(nums)
    
    return answer