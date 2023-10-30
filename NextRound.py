def next_round(sorted_leaderboard):
    table = [["White", "Black"]]
    for i in range(0, len(sorted_leaderboard) - 1, 2):
        table.append([sorted_leaderboard[i][0], sorted_leaderboard[i+1][0]])
    return table
