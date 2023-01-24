from collections import deque

def solution(n, wires):
    answer = -1

    def dfs(wire, start, wires, cnt, visit):
        visit[start] = 1
        for i in range(len(wires)):
            if wires[i] != wire:
                if wires[i][0] == start:
                    if visit[wires[i][1]] == 0:
                        visit[wires[i][1]] = 1
                        cnt.append(1)
                        dfs(wire, wires[i][1], wires, cnt, visit)
                if wires[i][1] == start:
                    if visit[wires[i][0]] == 0:
                        visit[wires[i][0]] = 1
                        cnt.append(1)
                        dfs(wire, wires[i][0], wires, cnt, visit)
        return cnt
    
    ans_list = []
    for wire in wires:
        a = dfs(wire, wire[0], wires, [1], [0] * (n+1))
        b = dfs(wire, wire[1], wires, [1], [0] * (n+1))
        ans_list.append(abs(sum(a)-sum(b)))
    answer = min(ans_list)
        
    return answer