def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for a in range(len(arr2[0])):
            tem = 0
            for b in range(len(arr2)):
                tem += arr1[i][b] * arr2[b][a]
            temp.append(tem)
        answer.append(temp)
    return answer