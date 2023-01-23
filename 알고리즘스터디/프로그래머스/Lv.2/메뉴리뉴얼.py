def solution(orders, course):
    answer = []
    
    food = set()
    for order in orders:
        for f in order:
            food.add(f)
    
    def dfs(l, food, visit, combo, combos, start):
        if len(combo) == l:
            combos.append(combo)
            return combos
        for i in range(start, len(food)):
            if visit[i] == 0:
                visit[i] = 1
                dfs(l, food, visit, combo + food[i], combos, i+1)
                visit[i] = 0
        return combos
    for l in course:
        food = sorted(list(food))
        visit = [0] * len(food)
        combo = ''
        combos = []
        start = 0
        combos = dfs(l, food, visit, combo, combos, start)
        combo_cnt = [0] * len(combos)
        for a in range(len(combos)):
            for i in range(len(orders)):
                match = 1
                for f in combos[a]:
                    if f not in orders[i]:
                        match = 0
                        break
                combo_cnt[a] += match
        max_cnt = max(combo_cnt)
        if max_cnt > 1:
            for i in range(len(combo_cnt)):
                if combo_cnt[i] == max_cnt:
                    answer.append(combos[i])
        else:
            break
    answer.sort()
    
    return answer