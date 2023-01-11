def solution(board, moves):
    answer = 0
    
    dolls = []
    for move in moves:
        for i in range(len(board)):
            num = board[i][move-1]
            if num != 0:
                board[i][move-1] = 0
                dolls.append(num)
                if len(dolls) == 1:
                    break
                else:
                    while dolls[-1] == dolls[-2]:
                        answer += 2
                        dolls.pop()
                        dolls.pop()
                        if len(dolls) < 2:
                            break
                    break
                
    return answer