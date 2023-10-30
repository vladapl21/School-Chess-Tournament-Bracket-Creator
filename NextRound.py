def next_round(sorted_leaderboard, round_num):
    if round_num % 2 == 0:
        table = [["Black", "White"]]
    else:
        table = [["White", "Black"]]
    for i in range(0, len(sorted_leaderboard) - 1, 2):
        table.append([sorted_leaderboard[i][0], sorted_leaderboard[i+1][0]])
    return table
