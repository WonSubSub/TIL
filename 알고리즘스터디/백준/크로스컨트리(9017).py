test_case = int(input())

for i in range(test_case):
    n = int(input())
    rank = list(map(int, input().split()))
    teams = set(sorted(rank))
    real_team = list(teams)
    for team_number in teams:
        if rank.count(team_number) < 6:
            real_team.remove(team_number)
            while rank.count(team_number) > 0:
                rank.remove(team_number)

    team_score = [0] * len(real_team)
    fifth_score = []
    for a in range(len(real_team)):
        count = 0
        for i in range(len(rank)):
            if real_team[a] == rank[i]:
                if count == 4:
                    fifth_score.append(i+1)
                    break
                team_score[a] += i+1
                count += 1
    
    min_index = team_score.index(min(team_score))
    ans = real_team[min_index]
    temp_fifth_score = 10000

    if team_score.count(min(team_score)) > 1:
        for i in range(len(team_score)):
            if team_score[i] == min(team_score):
                if fifth_score[i] < temp_fifth_score:
                    temp_fifth_score = fifth_score[i]
                    ans = real_team[i]
   
    print(ans)
