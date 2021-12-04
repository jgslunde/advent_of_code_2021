import numpy as np
filename = "input.dat"
draws = np.loadtxt(filename, delimiter=",", max_rows=1)
boards = np.loadtxt(filename, skiprows=2)
boards = boards.reshape((boards.shape[0]//5, 5, boards.shape[-1]))

def check_winners(boards):
    winners = []
    for i in range(len(boards)):
        board = boards[i]
        for rowcol in range(5):
            if (board[rowcol] == -999).all() or (board[:,rowcol] == -999).all():
                winners.append(i)
                break
    return winners

# Puzzle 1
for draw in draws:
    boards[boards == draw] = -999
    winners = check_winners(boards)
    if len(winners) > 0:
        winner_nr = winners[0]
        winner_board = boards[winner_nr]
        board_sum = np.sum(winner_board[winner_board >= 0])
        score = draw*board_sum
        print(winner_nr, winner_board, draw, board_sum, score)
        break


# Puzzle 2
winners_old = []
for draw in draws:
    boards[boards == draw] = -999
    winners = check_winners(boards)
    if len(winners) == len(boards):
        last_winner = (list(set(winners) - set(winners_old)))[0]
        winner_board = boards[last_winner]
        board_sum = np.sum(winner_board[winner_board >= 0])
        score = draw*board_sum
        print(last_winner, winner_board, draw, board_sum, score)
        break
    winners_old = winners