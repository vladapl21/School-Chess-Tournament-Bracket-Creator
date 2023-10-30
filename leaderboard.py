def leaderboard(players, points):
    # combine the two arrays
    table = []
    for i in range(len(players)):
        table.append([players[i], points[i]])
    return table


def bubblesort_2D(tosort):
    j = 0
    swap = True
    while swap == True:
        swap = False
        j += 1
        for i in range(len(tosort) - j):
            if tosort[i+1][1] > tosort[i][1]:
                swap = True  # shows that a swap has happened and another iteration takes place
                temp = tosort[i]
                tosort[i] = tosort[i + 1]
                tosort[i + 1] = temp

    return tosort
