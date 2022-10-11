"""
We're asked to imagine there is an algorithms tournament in which multiple teams 
compete against each other. In each competition there will be two teams that compete. 
There will be one winner and one loser out of all of these competitions and there are no ties. 
Each team will compete against all other teams exactly once. 
A team gets 3 points for each competition it wins and 0 points for each competition it loses. 
It's guaranteed that the tournament always has at least two teams and 
there will be only one tournament winner.

We are given two inputs, the competitions array and the results array. 
We need to write a function that returns the winner of the tournament, 
or more specifically, the name of the team that has the most number of points. 
The competitions array is an array of pairs,
representing all of the competitions in the tournament. 
Inside of these pairs, we have two strings: the first one is the name of the home team and 
the second one is the name of the away team. 
The results array represents the winner of each of these competitions. 
Inside the results array, a 1 means that the home team won and a 0 means the away team won. 
The results array is the same length as the competitions array, and 
the indices in the results array correspond with the indices in the competitions array.

examples:

input:
    competitions = [
    ["html", "c#"],
    ["c#", "python"],
    ["python", "html"]
    ]

    results = [0, 0, 1]

output: "python"

"""

HOME_TEAM_WON = 1

def tournament_winner(competitions: list, results: list):
    """
    A function that returns the winner of each of these competitions
    """
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team

def update_scores(team, points, scores):
    """
    update_scores
    """
    if team not in scores:
        scores[team] = 0

    scores[team] += points

print(tournament_winner(competitions=[["html", "c#"], ["c#", "python"], ["python", "html"]],results=[0, 0, 1]))