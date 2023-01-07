def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        i, j, k = map(int, commands[i])
        new_list = sorted(array[i-1:j])
        answer.append(new_list[k-1])
    return answer