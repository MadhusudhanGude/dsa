# O(N)T: N is number of competitions
# O(K)S: K is number of teams(at max)

def tourname_winner(competitions, results):
    top_team = ''
    points = {top_team: 0}

    for idx, competition in enumerate(competitions):
        home_team, away_team = competition
        home_team_won = results[idx]

        winning_team = home_team if home_team_won else away_team

        if not winning_team in points:
            points[winning_team] = 0

        points[winning_team] += 3

        if points[winning_team] > points[top_team]:
            top_team = winning_team
    return top_team


competitions = [['AUS', 'IND'],
                ['IND', 'NZ'],
                ['NZ', 'AUS']]
results = [0, 0, 1]
tourname_winner(competitions, results)
